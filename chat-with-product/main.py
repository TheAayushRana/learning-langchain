from ocr.reader import read_image
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_text_from_image(image_url):
    response = read_image(image_url)
    text = response['ParsedResults'][0]['ParsedText']
    return text

def chat_with_product(image_url):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    template = """
    You are a helpful assistant that can answer questions about a product.
    So you will be given information about the product which will have details about the product like name, ingredients and other details.
    You will then be given a question and you will need to answer it based on the product information.

    Here is the product information:
    {product_info}

    Question: {question}
    """

    prompt = PromptTemplate(input_variables=["product_info", "question"], template=template)

    chain = prompt | llm | StrOutputParser()

    product_info = get_text_from_image(image_url)

    result = chain.invoke({"product_info": product_info, "question": "Show product information in nice format"})

    return result

    # while True:
    #     user_input = input("Ask a question about the product (type 'exit' to quit): ")
    #     if user_input.lower() == 'exit':
    #         print("Exiting chat...")
    #         break
    #     result = chain.invoke({"product_info": product_info, "question": user_input})
    #     return result

if __name__ == '__main__':
    chat_with_product()