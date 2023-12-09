
#CourseCrafter 

CourseCrafter is a web application designed to revolutionize the way users discover courses tailored to their interests and needs. Leveraging the power of Python and Streamlit, this application employs natural language processing (NLP) techniques to recommend courses with precision. 


## HOW IT WORKS?

1. Vectorizing Course Descriptions 

CourseCrafter begins by transforming course descriptions into vectors of word counts. This is achieved through the utilization of a CountVectorizer object, converting textual information into numerical data that can be analyzed by machine learning algorithms. 

2. Cosine Similarity Analysis 

The heart of the recommendation system lies in the application of cosine similarity, a powerful NLP technique. Cosine similarity measures the likeness between two vectors, in this case, the word counts of the user's interests and the course descriptions. The higher the cosine similarity, the more akin the two vectors are. 

3. Personalized Recommendations 

By calculating the cosine similarity between the user's interests and course descriptions, CourseCrafter identifies the most similar courses. This personalized approach ensures that users receive recommendations aligned with their preferences and requirements. 
## Tech Stack used:


Python: The core programming language driving the application's functionality. 

Streamlit: A Python library that facilitates the creation of beautiful and interactive data applications. Streamlit enables an engaging user experience by simplifying the process of turning data scripts into shareable web apps. 
## Getting Started



To experience the power of CourseCrafter and explore personalized course recommendations: 

Clone the repository to your local machine. 

git clone https://github.com/your-username/CourseCrafter.git 
 

Install the necessary dependencies. 
pip install -r requirements.txt 
 
Run the application. 
streamlit run app.py 
Access the application through your web browser at http://localhost:8501. 
## Demo

Find the video link to demo attached below:

https://drive.google.com/file/d/1NjhLJN17xiSurtyK_KY8KB3wuvlr9svR/view?usp=sharing
