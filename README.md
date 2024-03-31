---
title: Capstone Project Documentation
---
## Description of what the project is for

The sentiment analysis Python script sentiment_analysis.py performs sentiment analysis on a dataset of customer reviews from Amazon.com using natural language processing (NLP) techniques. The script utilises the spaCy library for text preprocessing and sentiment analysis, along with the TextBlob library for sentiment polarity scoring.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Credits](#credits)
- [Contributing](#contributing)
## Features

- **Sentiment Analysis**: Analyses the sentiment of customer reviews to classify them as positive, negative, or neutral.
- **Text Preprocessing**: Cleans and preprocesses the review text by removing stopwords and punctuation.
- **Efficient Processing**: Processes large volumes of text data efficiently using spaCy's tokenisation and stop word removal capabilities.
- **Interpretable Results**: Provides clear and interpretable sentiment analysis results, allowing users to understand the sentiment of each review easily.

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python packages using pip:
   ```sh
   pip install pandas spacy textblob
   python -m spacy download en_core_web_md
   python -m textblob.download_corpora
   ```

## Usage

1. Ensure that the amazon_product_reviews.csv file containing the Amazon product reviews dataset is present in the same directory as the script.
2. Run the script sentiment_analysis.py.
3. The script will perform sentiment analysis on sample product reviews and display the results, including sentiment classification and similarity between reviews.

## Sample Output

```
Sample Review 1: I thought it would be as big as small paper but turn out to be just like my palm. I think it is too small to read on it... not very comfortable as regular Kindle. Would definitely recommend a paperwhite instead.
Sentiment: Negative

Sample Review 2: This kindle is light and easy to use especially at the beach!!!
Sentiment: Positive

Similarity between Review 1 and Review 2: 0.7609522586736197
```

## Credits

Developed by Elisha Patel

Data sourced from the [kaggle dataset](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews). 

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.