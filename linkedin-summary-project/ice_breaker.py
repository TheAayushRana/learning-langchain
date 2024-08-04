import os
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

information = """
    Jeffrey Preston Bezos (/ˈbeɪzoʊs/ BAY-zohss;[2] né Jorgensen; born January 12, 1964) is an American businessman, media proprietor and investor. He is the founder, executive chairman, and former president and CEO of Amazon, the world's largest e-commerce and cloud computing company. He is the second wealthiest person in the world, with a net worth of US$ 211 billion as of July 16, 2024, according to Forbes.[3] He was the wealthiest person from 2017 to 2021, according to both the Bloomberg Billionaires Index and Forbes.[4][5]

Bezos was born in Albuquerque and raised in Houston and Miami. He graduated from Princeton University in 1986 with degrees in electrical engineering and computer science. He worked on Wall Street in a variety of related fields from 1986 to early 1994. Bezos founded Amazon in mid-1994 on a road trip from New York City to Seattle. The company began as an online bookstore and has since expanded to a variety of other e-commerce products and services, including video and audio streaming, cloud computing, and artificial intelligence. It is the world's largest online sales company, the largest Internet company by revenue, and the largest provider of virtual assistants and cloud infrastructure services through its Amazon Web Services branch.

Bezos founded the aerospace manufacturer and sub-orbital spaceflight services company Blue Origin in 2000. Blue Origin's New Shepard vehicle reached space in 2015 and afterwards successfully landed back on Earth; he flew into space on Blue Origin NS-16 in 2021. He also purchased the major American newspaper The Washington Post in 2013 for $250 million and manages many other investments through his venture capital firm, Bezos Expeditions. In September 2021, Bezos co-founded Altos Labs with Mail.ru founder Yuri Milner.[6]

The first centibillionaire on the Forbes Real Time Billionaires Index and the second ever to have eclipsed the feat since Bill Gates in 1999, Bezos was named the "richest man in modern history" after his net worth increased to $150 billion in July 2018.[7] In August 2020, according to Forbes, he had a net worth exceeding $200 billion. On July 5, 2021, Bezos stepped down as the CEO and president of Amazon and took over the role of executive chairman. Amazon Web Services CEO Andy Jassy succeeded Bezos as the CEO and president of Amazon.
"""

if __name__ == '__main__':
    print("Hello World")
    # print("OPENAI_API_KEY" in os.environ)
    # print(os.environ['OPENAI_API_KEY'])
    print(os.environ['GOOGLE_API_KEY'])

    # information is here parameter
    summary_prompt = """
        for a given information {information} about a person i want you to create:
        1. Short summary
        2. two interesting facts about them
    """

    # prompt template takes input variable and template
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_prompt)

    # llm = ChatOpenAI(model='gpt-3.5-turbo', temperature= 0);
    # llm = ChatOllama(model='llama3')
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    chain = summary_prompt_template | llm | StrOutputParser()  # chain is a pipeline here | denotes pipe

    res = chain.invoke({"information": information})

    print(res)

