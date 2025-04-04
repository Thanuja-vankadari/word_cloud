This repository contains a Python script that generates a word cloud from the most frequent keywords found in 5-star reviews of apps in the "Health & Fitness" category. Common stopwords and app names are excluded.

Files Included

word_cloud.py - The Python script to generate the word cloud.

word_cloud.png - The output image of the word cloud.

app_reviews.csv - Sample dataset (not included, provide your own dataset with the required columns).

Installation and Usage

Prerequisites

Ensure you have Python installed along with the following libraries:

pip install pandas matplotlib wordcloud

Running the Script

Place your dataset (app_reviews.csv) in the same directory as word_cloud.py.

Run the script using:

python word_cloud.py

The word cloud image will be displayed and saved as word_cloud.png.

Dataset Requirements

The dataset should be a CSV file with the following columns:

Category (string) - Should contain "Health & Fitness" for filtering.

Rating (numeric) - Should be 5 for selecting 5-star reviews.

Review (string) - User review text.

App (string) - App name (used for exclusion).
