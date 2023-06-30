import streamlit as st

st.set_page_config(page_icon='📡', page_title="harley gray")
st.title("let's work together")


st.image('static/img/me.jpg', caption='being maximally cliche in America',width=210)
st.markdown("# about me")
st.write(
    """hi, my name is harley. my friends describe me as having "immaculate vibes" and as an "interesting person to talk to". i live in Brisbane, Australia
    """)
st.markdown("""
     i am driven by a desire to use technology for the common good. currently i am focussed on reducing the effectiveness of emotions-based campaigning in elections. to achieve this i am designing a framework to effectively store and use data so that voters have salient information when needed""")
    

st.markdown("# projects")
st.markdown("""## [your library](https://your-library.streamlit.app/)""")    

    
    
    
st.markdown("*use your data*")
st.markdown("""
a tool that enables data to be used effectively
by creating pipelines for classes of data, such as:
- policy platform documents
- interview transcripts
- essays and blog posts
- datasets; raw and analyzed

once a pipeline is defined, data can be added manually or automatically. for example, after each vote in parliament, a pipeline could:
1. download the vote count and breakdown
2. summarize and store the legislation
3. collect relevant metadata; e.g. financial interests of politicians/parties at the time, other legislation referenced, etc. 

with this information, voters could have more transparency into the political process. which leads to...
""")

st.markdown("""

## [Bot Hawke](https://twitter.com/BotHawke)
*cut the bullshit out of Australian politics by helping voters make informed desicions at elections* 

Bot Hawke is an example use case for your library. by recording parliament votes, interview transcripts and policy platforms, then making them readily accessible to voters in an understandable format, elections will become more issues-based. 

for any issue, e.g. environmental protections, voters will be able to see the actions taken and things said by each candidate on the ballot. 

my goal is to improve 100 people's understanding of Australia's upcoming [Voice to Parliament referendum](https://www.abc.net.au/news/2023-05-15/what-is-the-indigenous-voice-to-parliament-referendum-australia/102317242). next step is integrating key data schemas such as voting records and interview transcripts.  

""")

st.markdown("""
    # experience
    ### data analyst - **[Digital Surge](https://digitalsurge.com.au/)** (*2021-2022*)
    - increase profit margins by incorporating third party datasets into existing data, presenting in such a way as to enable agile updating of business practices
    - facilitate business understanding by developing dashboards through Google Cloud, and custom reports through Python/R to allow leadership to make data-driven decisions
    
    ### data assurance associate - **[PwC Australia](https://www.pwc.com.au/)** (*2023*)
    - uplift a data product by increasing profitability, streamlining processes and minimizing employee dependencies. the implementation of modern ETL pipelines and the reduction of complexity resulted in the product becaming net profitable
    - upskill team members in using LLMs by leading an initiative to create an AI product which ingests documents and allows semantic search 

    # education

    ### bachelor of mathematics (applied and computational) - **[Queensland University of Technology](https://www.qut.edu.au/courses/bachelor-of-mathematics-applied-and-computational-mathematics)** (*2018-2021*)
    - investigate online community building by using personal Twitter data to create maps and conduct analyses of my online network
    - verify that electrical componenents will not overheat by simulating the temperatures it will be exposed to
    - reconstruct images of the brain using fMRI data
    """
)
st.markdown("# skills")
with st.container():
    st.markdown("**python**")
    st.progress(value=0.85)
    st.markdown("**data lakes & warehousing**")
    st.progress(value=0.75)
    st.markdown("**ETL data pipelines**")
    st.progress(value=0.90)
    st.markdown("**deep learning**")
    st.progress(value=0.45)
    st.markdown("**R**")
    st.progress(value=0.70)


st.markdown("""
    # socials
    [GitHub](https://github.com/harleygray)

    [Twitter](https://twitter.com/harleyraygray)

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

