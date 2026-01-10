import streamlit as st

# Page config, page_title -> tab title, page_icon -> favicon, layout -> wide=container fulid, center=container (bootstrap)
st.set_page_config(page_title='Danish Javed',page_icon="👨🏻‍💻", layout='wide')

# h1 tag. Page title. Should be used only once
st.title("Streamlit Notes")
# Wrties muted text, great for providing containt
st.caption("A sample streamlit page to demo commonly used elements")
st.page_link(icon="🔗", page="https://www.devdanish.in", label="by Danish Javed", help="Learn more about the author")

# hr tag
st.divider()

# Consider it as section heading
st.header("Introduction")
st.write("""
    Streamlit is UI tool native to python. The prime purpose for this is to act as data presentation layer.  
    The prime benfit
    - seamless integration in python codebase
    - no seperate front end backend request cycles
    - super fast and easy UI development 
    """)

st.divider()

st.header("Getting started")
st.text("Here I'm writing the details of my learnings. I'll be using streamlit to note down my streamlit notes 😂🔥")

st.divider()

st.subheader("Installation")
st.text("Let's get started with installation first.")
col1, col2 = st.columns(2)
with col1:
    st.text(" Add \"streamlit\" in requirements.txt and run command below 👇🏻")
    st.code("pip install -r requirements.txt")
with col2:
    st.write("Or simply do ")
    st.code("pip install streamlit")

st.divider()

st.subheader("Page Setup")
st.text("""Like we have head in html, this our place to setup our page.""")
st.code(body="""import streamlit as st
st.set_page_config(page_title='Danish Javed',page_icon="👨🏻‍💻", layout='wide')""", language="python")
st.markdown("""
 Some simple optoins that we have 
 - page_title -> tab title
 - page_icon -> favicon
 - layout _(bootstrap analogy)_
    - wide = container fulid
    - center = container
""")

st.divider()

st.subheader("Page title")
st.caption("Typically used once per page")
st.text("Consider this as the page intro. Like headline of news or the title of our article. Below is what I have used for this page")
st.code(body="st.title(\"Streamlit Notes\")", language="python")

st.divider()

st.subheader("Headings")
st.text("In streamlit we have 2 heading options as header and subheader. Its intentional to keep it simple.")
header_col, subheader_col = st.columns(2)
with header_col:
    st.markdown("""##### Headers  
        
    - Translated to h2 tags
    - Mark heading of the section""")
    st.text("Like I have used for this section")
    st.code('st.header("Getting started")')
    pass
with subheader_col:
    st.markdown("""##### Subheaders  

        - Translated to h3 tags
        - Mark subheadings of the section""")
    st.text("Like I have used for this")
    st.code('st.subheader("Headings")')

st.divider()

st.subheader("Captions")
st.text("These are best to provide context for something. For ex, adds timeframe below a matrics etc")
st.text("Like I have used right below the page title")
st.code(body='st.context("A sample streamlit page to demo commonly used elements")')

st.divider()
st.subheader("Markdown")
st.text("Streamlit also provides the option to use markdown. We can render any markdown in out UI and it would work fine.")
st.text("I have been using this through out the page. Bullet points are the simple examples.")
st.code(language="python", body="""
 st.markdown(\"""##### Subheaders  

        - Translated to h3 tags
        - Mark subheadings of the section""\")""")
st.caption("Not just these but we can use all the markdown tags")