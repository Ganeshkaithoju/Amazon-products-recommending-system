import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Product Recommendation System")
st.write("Pick an Amazon product and I will show similar products "
         "(based on name, category and description).")


@st.cache_resource          # runs only once, not on every click
def load_data():
    products = pd.read_csv("products_clean.csv")
    products["clean_text"] = products["clean_text"].fillna("")    # empty text is read as NaN
    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    tfidf_matrix = tfidf.fit_transform(products["clean_text"])
    return products, tfidf_matrix


products, tfidf_matrix = load_data()


def recommend(item_name, top_n=5):
    idx = products.index[products["product_name"] == item_name][0]
    scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).ravel()   # only this product's row
    order = scores.argsort()[::-1]
    order = order[order != idx][:top_n]
    return products.iloc[order].assign(score=scores[order])


product_name = st.selectbox("Select a product:", products["product_name"].values)

if st.button("Recommend"):
    st.subheader("You may also like:")
    for rank, (_, p) in enumerate(recommend(product_name).iterrows(), start=1):
        rating = "N/A" if pd.isna(p["rating"]) else p["rating"]
        name = p["product_name"].replace("[", "(").replace("]", ")")     # [ ] would break the markdown link
        st.markdown(f"**{rank}. [{name}]({p['product_link']})**") # my dataset consists of product links, using the same to create redirections
        st.caption(f"{p['short_category']} | Price: {p['discounted_price']} | "
                    f"Rating: {rating} | Similarity: {p['score']:.2f}")