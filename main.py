
import streamlit as st 
import streamlit.components.v1 as stc
import streamlit as st



# Apply background image using st.markdown


import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel

def load_data(data):
	df = pd.read_csv(data)
	return df 


def vectorize_text_to_cosine_mat(data):
	count_vect = CountVectorizer()
	cv_mat = count_vect.fit_transform(data)
	# Get the cosine
	cosine_sim_mat = cosine_similarity(cv_mat)
	return cosine_sim_mat


@st.cache_resource
def get_recommendation(title,cosine_sim_mat,df,num_of_rec=10):
	
	course_indices = pd.Series(df.index,index=df['Course Name']).drop_duplicates()
	
	idx = course_indices[title]

	
	sim_scores =list(enumerate(cosine_sim_mat[idx]))
	sim_scores = sorted(sim_scores,key=lambda x: x[1],reverse=True)
	selected_course_indices = [i[0] for i in sim_scores[1:]]
	selected_course_scores = [i[0] for i in sim_scores[1:]]


	result_df = df.loc[selected_course_indices]
	result_df['similarity_score'] = selected_course_scores
	final_recommended_courses = result_df[['Course Name','University','Course URL','Course Rating','Difficulty Level',]]
	return final_recommended_courses.head(num_of_rec)

RESULT_TEMP = """
<div style="width:90%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 60px;
box-shadow:0 0 15px 5px #ccc; background-color:rgb(245,245,220,0.5);border-left: 5px solid #6c6c6c;">
<h4>{}</h4>
<p style="color:blue;"><span style="color:black;">University:</span>{}</p>
<p style="color:blue;"><span style="color:black;">🔗</span><a href="{}",target="_blank">Link</a></p>
<p style="color:blue;"><span style="color:black;">Rating:</span>{}</p>
<p style="color:blue;"><span style="color:black;">🧑‍🎓👨🏽‍🎓 Difficulty Level:</span>{}</p>

</div>
"""
@st.cache_resource
def search_term_if_not_found(term,df):
	result_df = df[df['Course Name'].str.contains(term)]
	return result_df


def main():
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://images.unsplash.com/photo-1488998427799-e3362cec87c3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80");
    background-size:cover;
    background-position: top left;
    background-repeat: no-repeat;
    
    }}

    
   
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
   
    title = '<h1 style="font-family:sans-serif; color:#5c2f1b; font-size: 100px; font-weight: 900">CourseCrafter</h1>'
    st.markdown(title, unsafe_allow_html=True)
    menu = ["Home", "Recommend", "About"]
    
    choice = st.sidebar.selectbox(":color[Menu]", menu)

    df = load_data("data/Coursera.csv")
    


    



    if choice == "Home":

        title = '<h2 style="font-family:Amatic SC; color:#5c2f1b; font-size: 50px; font-weight:100">Home</h2>'
        para='<h6 style="font-family:Sans Serif;color:#ed092c;font-size: 30px;font-weight:100">List Of Courses</h6>'
        st.markdown(title, unsafe_allow_html=True)
        st.markdown(para, unsafe_allow_html=True)
        menu = ["Home", "Recommend", "About"]
    
        st.markdown(
        f"""
        <style>
            
            .dataframe td {{
                color: blue;  
            }}
        </style>
        """,
        unsafe_allow_html=True
        )
        st.dataframe(df.head(10))

    elif choice == "Recommend":
        title = '<h2 style="font-family:Amatic SC; color:#5c2f1b; font-size: 50px; font-weight:100">Recommend</h2>'
        st.markdown(title, unsafe_allow_html=True)
        cosine_sim_mat = vectorize_text_to_cosine_mat(df['Course Name'])
        search_term = st.text_input(":red[Search]")
        num_of_rec = st.sidebar.number_input("Number", 4, 30, 7)
        if st.button("Recommend"):
            if search_term is not None:
                try:
                    results = get_recommendation(search_term, cosine_sim_mat, df, num_of_rec)

                    if not results.empty:
                        with st.expander(":blue[Results as JSON]"):
                            results_json = results.to_dict('index')
                            st.write(results_json)

                        for row in results.iterrows():
                            rec_title = row[1]['Course Name']
                            
                            rec_url = row[1]['Course URL']
                            rec_price = row[1]['Course Rating']
                            rec_diff=row[1]['Difficulty Level']
                            rec_uni = row[1]['University']

                            stc.html(RESULT_TEMP.format(rec_title, rec_url,rec_price,rec_diff,rec_uni),
                                     height=350)
                    else:
                        st.warning("No courses found.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.info(":brown[Suggested Options include]")
                    result_df = search_term_if_not_found(search_term, df)
                    st.dataframe(result_df)
    else:
        title = '<h2 style="font-family:Amatic SC; color:#5c2f1b; font-size: 50px;font-weight:`100">About</h2>'
       
        para='<h6 style="font-family:Sans Serif;color:#ed092c;font-size: 30px;font-weight:100">Welcome to our CourseCrafter! We are thrilled to have you here and share a little about who we are and what we do.</h6>'
        st.markdown(title, unsafe_allow_html=True)
       
        st.markdown(para,unsafe_allow_html=True)
        
if __name__ == '__main__':
    main()
