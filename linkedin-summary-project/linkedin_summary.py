from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import fetch_linkedin_data

if __name__ == '__main__':
    print("Hello World")
    summary_prompt = """
        for a given Linkedin information {information} about a person i want you to create:
        1. Short summary
        2. two interesting facts about them
    """

    # prompt template takes input variable and template
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_prompt)

    # llm = ChatOpenAI(model='gpt-3.5-turbo', temperature= 0);
    llm = ChatOllama(model='llama3')

    chain = summary_prompt_template | llm | StrOutputParser()  # chain is a pipeline here | denotes pipe

    linkedin_data = fetch_linkedin_data()

    res = chain.invoke({ "information": linkedin_data })

    print(res)
