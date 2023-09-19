import streamlit as st

st.set_page_config(page_icon='📡', page_title="harley gray")
st.title("let's work together")


st.image('static/img/me.jpg', caption='being maximally cliche in America',width=210)
st.markdown("# about me")
st.write(
    """hi, my name is harley. my friends describe me as having "immaculate vibes" and an "interesting person to talk to". i live in Brisbane, Australia
    """)
st.markdown("""
     i am driven by a desire to use technology for the common good. currently i am focussed on reducing the effectiveness of emotions-based campaigning in elections. to achieve this i am designing a framework to effectively store and use data so that voters have salient information when needed""")
    

st.markdown("# projects")
st.markdown("""## [your library](https://your-library.streamlit.app/)""")    
st.markdown("""
    a tool to help Australians do their own research for the upcoming referendum.
    my goal is to have 100 people use this tool to understand Australia's upcoming [Voice to Parliament referendum](https://www.abc.net.au/news/2023-05-15/what-is-the-indigenous-voice-to-parliament-referendum-australia/102317242)

    curated sources from the Yes and No campaigns are made available via a chat interface, where users can ask a question such as "what is the Voice to Parliament and what will it do?" and have an answer summarised from sources like:
    - the official Australian Electoral Comission's booklet 
    - information booklets from the Yes and No campaigns
    - indepentent scholarly reviews of the proposed Constitutional amendment
""")


st.markdown("""
    # experience
    ### data analyst - **[Digital Surge](https://digitalsurge.com.au/)**
    - provide advice on business decisions by undertaking statistical exploration (e.g. Monte-Carlo simulations, hypothesis testing, network analysis) on available data, then explaining results using the appropriate  level of detail
    - enhance business understanding across the company by determining the data-related questions of each department (executive, customer service, marketing) and creating ongoing solutions based on their needs
    
    ### data assurance associate - **[PwC Australia](https://www.pwc.com.au/)** 
    - deliver outcomes for clients by understanding their business requirements and utilizing a suite of data processing technologies (e.g. Python, SQL, Alteryx) to deliver presentations, reports and dashboards   
    - upskill team members in using LLMs by leading an initiative to create a document chatbot. Manage the team by assigning coding tasks suiting their programming experience, resulting in a working prototype 
    - translate business requirements into data products in collaboration with both technical and non-technical stakeholders

    # education
    ### Arize.ai - [Machine Learning Observability](https://arize.com/blog-course/)
    - provide accurate and contextually relevant responses to user questions by deploying a fine-tuned LLM and monitoring to ensure that quality improves over time
    ### Fast.ai - [Practical Deep Learning for Coders](https://course.fast.ai/)
    - build and train deep learning models for NLP and computer vision tasks by leveraging current deep learning techniques and software (e.g. PyTorch, fastai)
    - develop, evaluate and deploy models from scratch and iterate to improve performance
    ### Queensland University of Technology  - [Bachelor of Mathematics (applied and computational)](https://www.qut.edu.au/courses/bachelor-of-mathematics-applied-and-computational-mathematics)
    - investigate online community building by using personal Twitter data to create maps and conduct analyses of my online network
    - verify that electrical componenents will not overheat by simulating the temperatures it will be exposed to
    - reconstruct images of the brain using fMRI data
    """
)
st.markdown("# skills")
with st.container():
    st.markdown("**python**")
    st.progress(value=0.90)
    st.markdown("**natural language processing**")
    st.progress(value=0.80)
    st.markdown("**data lakes & warehousing**")
    st.progress(value=0.75)
    st.markdown("**ETL data pipelines**")
    st.progress(value=0.90)
    st.markdown("**deep learning**")
    st.progress(value=0.55)
    st.markdown("**R**")
    st.progress(value=0.70)


st.markdown("""
    # socials
    [GitHub](https://github.com/harleygray)

    [Twitter/X](https://twitter.com/harleyraygray)

    [LinkedIn](https://linkedin.com/in/harleygray1996)

    Email: harley.gray.96@gmail.com
""")


#st.text('Fixed width text')
#st.markdown('_Markdown_') # see *
#st.latex(r''' e^{i\pi} + 1 = 0 ''')
#st.write(['st', 'is <', 3]) # see *
#st.title('My title')
#st.header('My header')
#st.code('for i in range(8): foo()')
#st.subheader('My sub')

