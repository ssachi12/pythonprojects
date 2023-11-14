import streamlit as st
import newspaper


st.title('Article scraper')
url=st.text_input('enter the url', placeholder='paste url and enter')

if url:
    article=newspaper.Article(url)
    article.download()

    article.parse()
    authors=article.authors
    st.text(','.join(authors))


    # article.nlp()

    tab1, tab2 =st.tabs(['Full text', 'Summary'])

    with tab1:
        article.text
    with tab2:
        st.text("Nothing")
