import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Load dataset (update with the correct file path)
df = pd.read_csv("app_reviews.csv")

# Filter for Health & Fitness apps and 5-star reviews
df_filtered = df[(df['Category'] == 'Health & Fitness') & (df['Rating'] == 5)]

# Combine all review texts
text = " ".join(review for review in df_filtered['Review'].dropna())

# Define stopwords and add app names (customize as needed)
stopwords = set(STOPWORDS)
app_names = set(df_filtered['App'].unique())
stopwords.update(app_names)

# Generate word cloud
wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Save word cloud image
wordcloud.to_file("word_cloud.png")
