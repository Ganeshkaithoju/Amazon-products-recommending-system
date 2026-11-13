# Product Recommendation System (Content-Based)

A simple Streamlit app that recommends similar Amazon products.
Pick a product from the dropdown, click **Recommend**, and it shows the 5 most similar products.

**Dataset:** Amazon Sales Dataset (Kaggle) - https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset
(1,465 rows -> 1,337 unique products after removing repeats)

## How it works

1. Text = product name + category + description
2. Clean it: lowercase, remove punctuation/special characters, remove stopwords, missing values -> empty string
3. TF-IDF (`max_features=5000`, `ngram_range=(1, 2)`)
4. Cosine similarity between the selected product and all other products
5. Show the top 5

## Files


| File                          | What it is                                                            |
| ------------------------------- | ----------------------------------------------------------------------- |
| `assignment20_recommender.py` | data loading, cleaning, TF-IDF, similarity, `recommend()` (Tasks 1-5) |
| `app.py`                      | Streamlit app (Task 6)                                                |
| `products_clean.csv`          | cleaned text, created by the script above, used by the app            |
| `requirements.txt`            | libraries for deployment                                              |

## Run on your computer

```bash
pip install -r requirements.txt
python assignment20_recommender.py      # only needed to re-create products_clean.csv (needs amazon.csv)
streamlit run app.py
```

## Push to GitHub (Task 7)

Create an EMPTY repo on github.com (no README), then in this folder:

```bash
git init
git add .
git commit -m "product recommender: pipeline + streamlit app"
git branch -M main
git remote add origin https://github.com/<your-username>/product-recommender.git
git push -u origin main
```

(GitHub does not accept the account password on push, use a Personal Access Token or GitHub CLI / Desktop.)

## Deploy on Render (Task 8)

1. Sign up on https://render.com with GitHub
2. **New +** -> **Web Service** -> pick the `product-recommender` repo
3. Settings:
   - Runtime: **Python 3**
   - Branch: `main`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true`
   - Instance type: **Free**
4. Environment variable (recommended): `PYTHON_VERSION` = `3.11.9`
5. **Create Web Service**, wait for the build, open the `https://....onrender.com` link

Free instances sleep when idle, so the first open can take about a minute. Every `git push` to `main` re-deploys.

## Final validation (Task 9)

- [ ]  Deployed page opens and the dropdown has ~1,337 products
- [ ]  Pick a Wayona cable -> other Wayona cables at the top
- [ ]  Pick a Prestige kettle -> other electric kettles
- [ ]  Pick a boAt Bassheads earphone -> other boAt earphones
- [ ]  Results match the output of `assignment20_recommender.py`

**Deployed URL:** _paste here_
**GitHub repo:** _paste here_
