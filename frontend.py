import streamlit as st
from utils import get_prediction
import pandas as pd

st.set_page_config(page_title="Hate Speech with Modular Pipelines", page_icon="😾")

st.title('Hate Speech detection with Modular Pipelines')
st.subheader('Interactive frontend to the API')

sad_img= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRm8NnfldcgEdYwWwDnDtjanI61Nq33Y_Ag3g&usqp=CAU"
happy_img= "https://i.guim.co.uk/img/media/7a2f365685c03860db34e122bc5165a01874dfde/0_112_5093_3055/master/5093.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=66a0eedff1916b274c39b8b781441a10"



with st.form("my_form"):
    text = st.text_input('Code to analyze', 'def hello(a):\nreturn a')
    submitted = st.form_submit_button("Predict")
    
    # pipeline = st.radio(
    #     "Which pipeline should we use?",
    #     ('random', 'all_0s', 'all_1s', 'sklearn_simple_nb'))
    
    
    if submitted:
        with st.spinner('Wait for it...'):
            data = get_prediction(text)
            
        if data:
            st.subheader("Prediction(s)")
            
            # df = pd.DataFrame.from_dict({"input_text":text, "prediction": data})
            
            # df = df.to_html(render_links=True,escape=False,col_space=100)
            
            st.text(f'Closest matches are:')
            st.text(f'------')
            st.text(text)
            st.text(f'------')
            st.markdown(data, unsafe_allow_html=True)
            # st.markdown(df, unsafe_allow_html=True)
            
        else:
            st.error("Error")


# '''
# # Using the Hate-Speech-Api

# The root URL to the API is: ``https://hatespeech-api.herokuapp.com/``

# ## Prediction endpoint (get)

# Returns the category for a given text(s) using the desired trained pipeline.

# \tReturn values:
# \t0 - not hate-speech or 
# \t1 - hate-speech for the given text

# - Endpoint url: ``/detect``
# - Required params: ``text`` and ``pipeline_name``
#     You can query multiple text at the same time by adding a ``;`` delimiter between the texts.

# - Construction of the get request: 
#     ``root_url`` + ``/detect?`` + ``text=This is an example tweet`` + ``&`` + ``pipeline_name=random``
# - example: ``https://hatespeech-api.herokuapp.com/detect?text=This is an example tweet&pipeline_name=random``


# ## Pipeline hierarchy endpoint (get)

# Returns the structure of the pipeline queried.

# - Endpoint url: ``/pipeline``
# - Required params: ``pipeline_name``

# - example: ``https://hatespeech-api.herokuapp.com/pipeline?pipeline_name=random``


# # About Modular Pipelines
# Hate Speech detection was built on **``Modular Pipelines (mopi)``**, a lightweight & extensible library 
# to create complex multi-model and multi-modal pipelines, including ``Ensembles`` and ``Meta-Models``

# Check the project out on [GitHub Repo](https://github.com/applied-exploration/modular-pipelines).  
# '''
