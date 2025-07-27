import matplotlib.pyplot as plt
import streamlit as st

def show_movie_vs_tv_chart(df,option):
    st.subheader(option)
    fig, ax = plt.subplots()
    c1, c2 = st.columns(2)
    with c1:
        total_movies = df['type'].value_counts().get('Movie', 0)
        st.subheader(f'Total Movies: {total_movies}')
    with c2:
        total_tv_shows = df['type'].value_counts().get('TV Show', 0)
        st.subheader(f'Total TV Shows: {total_tv_shows}')
    movie_vs_tv = df['type'].value_counts()
    ax.pie(movie_vs_tv, labels=movie_vs_tv.index, autopct='%1.1f%%')
    st.pyplot(fig)

    st.subheader('Top Countries by Content')
    top_countries = df['country'].value_counts().head(10)
    fig2, ax2 = plt.subplots()
    ax2.bar(top_countries.index, top_countries.values, color='green')
    ax2.set_title("Top 10 Countries", fontsize=14, color='red')
    ax2.set_xlabel("Country", color='blue')
    ax2.set_ylabel("Content Count", color='blue')
    st.pyplot(fig2)


    st.subheader('Bar Chart – Content count by Rating')
    rating = df['rating'].value_counts().head(10)
    fig3, ax3 = plt.subplots()
    ax3.bar(rating.index, rating.values, color='#E75480')
    ax3.set_title("Content Count by Rating", color='blue')
    ax3.set_xlabel("Rating", color='red')
    ax3.set_ylabel("Number of Titles", color='red')
    st.pyplot(fig3)

    st.subheader('Year-wise release trend – Line chart')
    yearly_trend = df['year'].value_counts().sort_index()
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    ax4.plot(yearly_trend.index, yearly_trend.values, marker='o', color='green')
    ax4.set_title('Year-wise Release Trend', color='green', fontsize=20)
    ax4.set_xlabel("Year", fontsize=19, color='blue')
    ax4.set_ylabel("Number of Titles", fontsize=20, color='blue')
    ax4.grid(True)
    st.pyplot(fig4)

