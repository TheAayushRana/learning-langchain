from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain.agents import (
    create_react_agent, # it is built in function to create agent
    AgentExecutor # it is built in class to execute agent
)
from langchain import hub
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools.tavily_search import TavilySearchResults
from langchain_core.output_parsers import StrOutputParser

def get_profile_url_travily(name):
    search = TavilySearchResults()
    results = search.run(f"{name}")

    return results[0]['url']

def linkedin_lookup(profile_name: str):

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0, 
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    template = """
        You are a helpful assistant that can look up profiles on LinkedIn.
        You are given a full name {name_of_person} and i want you to get link of their linkedin profile page.
        Your answer should only contain the url of the profile page.
    """

    prompt_template = PromptTemplate(
        template=template,
        input_variables=['name_of_person']
    )

    # it contains all the tools that agent can use
    tools_for_agent = [
        Tool(
            name='Crawl google for linkedin profile url',
            description='useful to get url of linkedin profile page',
            func=get_profile_url_travily
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    # used to create agent
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )

    # used to execute agent
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=profile_name)})

    linkedin_profile_url = result['output']

    return linkedin_profile_url

if __name__ == "__main__":
    linkedin_url = linkedin_lookup(profile_name='Aayush Rana Lorien Finance GTBIT')
    print(linkedin_url)