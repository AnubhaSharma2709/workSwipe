from langchain.prompts import PromptTemplate 
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain 
from third_parties.linkedin import scrape_linkedin_profile
import os 

information ="""
When Modi was eight years old, he was introduced to the Rashtriya Swayamsevak Sangh (RSS) and began attending its local shakhas (training sessions). There, he met Lakshmanrao Inamdar, who inducted Modi as a balswayamsevak (junior cadet) in the RSS and became his political mentor.[51] While Modi was training with the RSS, he also met Vasant Gajendragadkar and Nathalal Jaghda, Bharatiya Jana Sangh leaders who in 1980 helped found the BJP's Gujarat unit.[52]"
"""
if __name__ == '__main__':
    print("Hello World")

    summary_template = """
    I want you to create a short summary of the given information {information}
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )
    
    chain = LLMChain(
        llm=llm,
        prompt=summary_prompt_template
    )
    
    linkedin_data = scrape_linkedin_profile(profile_url="https://www.linkedin.com/in/divyanshu-rana-792a03223/")
    
    print(chain.run(information= linkedin_data ))
