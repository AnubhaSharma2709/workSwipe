from langchain.prompts import PromptTemplate 
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain 
from third_parties.linkedin import scrape_linkedin_profile
import os 
from agents.linkedin_lookup import lookup as linkedin_lookup_agent 
from output_parse import person_intel_parser , PersonIntel
def ice_break(name: str)-> PersonIntel:
    summary_template = """
    Given the LinkedIn Information{information} about [User's Name], I want you to create the following summary:
    
1. **Profile Summary:**
   - [User's LinkedIn summary]

2. **Interesting Topics:**
   - Based on the user's LinkedIn activity, the following topics seem to be of interest:
     - [Topic 1]
     - [Topic 2]
     - [Topic 3]

3. **Number of Posts Liked - Showing Activities on LinkedIn:**
   - Total Posts Liked: [Number of posts liked]
   - Posts Commented On: [Number of posts commented on]
   - Posts Shared: [Number of posts shared]
   - Post Likes Over Time: [A time series graph showing post likes over time]

4. **Profile Information:**
   - Name: [User's Name]
   - Current Position: [User's current position]
   - Location: [User's location]
   - Connections: [Number of connections]
   - Industry: [User's industry]
   - Recommendations: [Number of recommendations]
   - Total Posts: [Number of total posts]
   - Followers: [Number of followers]
   - Connections:[Number of Connections]
   \n{format_instructions}
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_.format_instructions()
            }
    )
    
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )
    
    chain = LLMChain(
        llm=llm,
        prompt=summary_prompt_template
    )
    linkedin_profile_url= linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(profile_url= linkedin_profile_url)
    
    results=chain.run(information = linkedin_data)
    return person_intel_parser.parse(results)


if __name__ == '__main__':
    print("Hello World!")
    results = ice_break(name ="dr-shalini-sharma-24450914")

    
