from langchain.prompts import PromptTemplate 
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain 
from third_parties.linkedin import scrape_linkedin_profile
import os 
from agents.linkedin_lookup import lookup as linkedin_lookup_agent 


information =" "
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
    linkedin_profile_url= linkedin_lookup_agent(name="divyanshu-rana-792a03223")
    linkedin_data = scrape_linkedin_profile(profile_url= linkedin_profile_url)
    
    print(chain.run(information= linkedin_data))
