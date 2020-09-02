# This file contains the code for functions used in "Topic Modeling to Identify Women's Health Concerns"
# Functions are organized by section of the project

### DATA CLEANING ###
def create_total_text(df):
    df['total_text'] = df['title'] + ' ' + df['selftext']
    df.drop(columns = ['title', 'selftext'], inplace = True)
    return df.head(1)

def clean_columns(df):
    '''Drops columns from specified data frame'''
    df.drop(columns = ['created_utc', 'num_comments', 'score', 'is_self'], inplace = True)

def display_percent_null(df):
    '''Returns the percent of values in each column that are null or missing'''
    return (df.isna().sum()/len(df)) * 100

def convert_to_datetime(df, column):
    '''Converts column to a datetime object'''
    df[column] = pd.to_datetime(df[column])
    return df.dtypes

def remove_string(df, column, string):
    '''Replaces the input string with an empty string'''
    df[column] = df[column].str.replace(string, '')
    return df.head(1)

def remove_urls(df, column):
    '''Uses regex to substitute urls with an empty string'''
    for i in range(0, len(df)):
        df.loc[i, column] = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', df.loc[i, column])
# Regex Code for remove_urls by Lee Martin (Stack Overflow post)
# https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python/11332580   

def delete_empty_text(df, column):
    '''Filters data frame to exclude any columns with empty strings'''
    df = df[df[column] != '']
    return df.shape

def remove_AutoModerator(df, column):
    '''Filters df to exclude the 'AutoModerator' author''' 
    df = df[df[column] != 'AutoModerator']
    return df

def remove_digits(df, column1):
    '''Replaces digits with empty strings'''
    df[column1] = df[column1].str.replace('[0-9]+', '', regex = True)


### TEXT PREPROCESSING ###
def add_stop_words(word_list, list_stop_words):
    '''Adds a list of words to a list of stop words'''
    for word in word_list:
        list_stop_words.add(word)

def remove_stop_words(word_list, list_stop_words):
    '''Removes a list of words from a list of stop words'''
    for word in word_list:
        list_stop_words.remove(word)

def get_word_count(df, column, new_column = 'word_count'):
    '''Calculates word count and saves it to a 'word_count' column'''
    df[new_column] = df[column].apply(lambda x: len(x.split()))
    return df.head(1)

def tokenize_and_lemma(df, column, stop_words = full_stop_words):
    '''Takes a string and returns a lemmatized version of the string'''
    nlp = spacy.load('en_core_web_sm')
    
    lemma_tokens = []
    
    for post in df[column]:
        doc = nlp(post) # Run text through spaCy pipeline
        tokens = [token for token in doc if token.text not in stop_words]
        lemma_tokens.append([token.lemma_ for token in tokens])

    df['lemma_text'] = [' '.join(post) for post in lemma_tokens] # join tokens back together into string
        
    return df.head()

def analyze_sentiment(df, column, new_column = 'sentiment_score', score = 'compound'):
    '''Returns VADER composite sentiment score for a string'''
    sent_anal = SentimentIntensityAnalyzer()
    sentiment_scores = [sent_anal.polarity_scores(post)[score] for post in df[column]]
    df[new_column] = sentiment_scores
    return df.head()


### EXPLORATORY DATA ANALYSIS ###
def unique_authors(df, column, title):
    '''Returns count of unique entries for a column'''
    return f'{title} has {df[column].nunique()} unique authors.'

def subplot_histogram(data, axis, title = None, x_label = None, y_label = None, color = None):
    '''Creates a subplot of a histogram'''
    sns.distplot(data, ax = axis, kde = False, hist_kws=dict(edgecolor="k", linewidth=.9, alpha = 0.9), color = color)
    axis.set_title(title, pad = 8, fontdict = {'fontsize':14})
    axis.set_xlabel(x_label, labelpad = 6, fontdict = {'fontsize':13})
    axis.set_ylabel(y_label, labelpad = 6, fontdict = {'fontsize':13})
    axis.tick_params(axis = 'both', labelsize = 11)
    plt.tight_layout();

def get_word_vector(data, ngrams = (1,1), stopwords = None, min_df = 0.001):
    '''Returns a data frame of a bag of words for the input data '''
    cvec = CountVectorizer(stop_words = stopwords, ngram_range = ngrams, min_df = min_df)
    words = cvec.fit_transform(data)
    df = pd.DataFrame(words.toarray(), columns = cvec.get_feature_names())
    return df

def get_word_sums(words_df):
    '''Creates a data frame with total word counts in the data'''
    word_sum = {}
    for column in words_df.columns:
        word_sum[column] = words_df[column].sum()
    df = pd.DataFrame(sorted(word_sum.items(), key = lambda x: x[1], reverse = True), columns = ['Word', 'Count'])
    return df.sort_values('Count', ascending = False)

def plot_top_words(word_count_df, num_words = 10, title = None, x_label = None, y_label = None, color = None):
    '''Creates a bar plot of the n most frequent words in the data'''
    sns.barplot(y = word_count_df['Word'][:num_words], x = word_count_df['Count'][:num_words], orient = 'h', color = color, edgecolor = 'black')
    plt.title(title, fontdict = {'fontsize':15}, pad = 12)
    plt.xlabel('Count', fontdict = {'fontsize':13}, labelpad = 10)
    plt.ylabel('Word', fontdict = {'fontsize':13}, labelpad = 10)
    plt.tight_layout;

### MODEL PREPARATION ###

### MODELING ###

### MODEL SELECTION AND EVALUATION ###
