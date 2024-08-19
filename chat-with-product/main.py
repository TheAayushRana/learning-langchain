from ocr.reader import read_image
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_text_from_image(image_url):
    response = read_image(image_url)
    text = response['ParsedResults'][0]['ParsedText']
    return text

if __name__ == '__main__':
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

    product_info = get_text_from_image("https://i.imghippo.com/files/ngMbQ1724048156.png")

    # result = chain.invoke({"product_info": product_info, "question": "What all ingredients does this product contain?"})

    while True:
        user_input = input("Ask a question about the product (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting chat...")
            break
        result = chain.invoke({"product_info": product_info, "question": user_input})
        print(result)