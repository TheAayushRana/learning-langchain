from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

if __name__ == "__main__":
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

    query = "what is langchain-pinecone?"
    prompt_template = PromptTemplate(input_variables=[], template=query)

    chain = prompt_template | llm

    # res = chain.invoke({ "input": "" })

    vectorstore = PineconeVectorStore(index_name="basic-rag-project", embedding=embeddings)

    # prompt for retrieving
    retriever_qa_chat_prompt = hub.pull('langchain-ai/retrieval-qa-chat')

    # create_stuff_documents_chain- This chain takes list of documents and formats them into a single document and then passes it to
    # the LLM for further processing.
    combined_docs_chain = create_stuff_documents_chain(llm, retriever_qa_chat_prompt)

    # create_retriever_chain- This chain takes a query, passes it to the retriever, retrieves a list of documents, and then passes
    retriever_chain = create_retrieval_chain(retriever=vectorstore.as_retriever(), combine_docs_chain=combined_docs_chain)

    result = retriever_chain.invoke({ "input": query })

    print(result)

    # template = """
    #     Use the following context to answer the question at the end:
    #     If you don't know the answer, just say "I don't know" don't try to make up an answer.
    #     and at last always say "Thanks for answering my question" at the end.

    #     {context}
        
    #     Question: {question}
    # """

    # custom_rag_prompt = PromptTemplate.from_template(template)

    # rag_chain = (
    #     {"context": vectorstore.as_retriever() | format_docs, "question": RunnablePassthrough()} | custom_rag_prompt | llm
    # )

    # result = rag_chain.invoke(query)

    # print(result)
