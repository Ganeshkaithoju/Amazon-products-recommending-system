# Product Recommendation System

A simple web app that suggests similar Amazon products. Pick a product from the dropdown, click **Recommend**, and get the 5 closest matches with their price, rating, similarity score and a link to the product page.

**Live demo:** <your-deployed-url>

## How it works

This is a **content-based** recommender. It compares what products are *about*, not what other users bought.

1. **Text:** the product name, category and description are joined into one text per product.
2. **Cleaning:** lowercase, remove punctuation and special characters, remove stopwords.
3. **TF-IDF:** each product becomes a vector of weighted words and word pairs (up to 5,000 features), so distinctive words count more than common ones.
4. **Cosine similarity:** the selected product is compared with every other product, and the highest scores are shown.

Example: picking a Prestige electric kettle returns other Prestige kettles first, then similar kettles from other brands.

## Dataset

[Amazon Sales Dataset](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset) from Kaggle. After removing repeated products, about 1,300 unique products are used.

## Tech stack

Python, pandas, scikit-learn, Streamlit

## Run locally

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install -r requirements.txt
streamlit run app.py
```

The app opens at http://localhost:8501.

## Project files

| File | Purpose |
|---|---|
| `app.py` | Streamlit app |
| `products_clean.csv` | Cleaned product text used by the app |
| `requirements.txt` | Python dependencies |

## Limitations

- Product names are part of the text, so results lean towards the same brand or model.
- Recommendations come only from text, so price and rating do not affect them.
