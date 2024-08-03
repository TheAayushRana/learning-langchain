pipenv shell- package manager and virtual environment - It contains all the dependencies that we need to run the project
pipenv install langchain

langchain is a framework which is used to create ai application by integrating and intracting with llm models.

chain of actions

langchain package is split into 3 packages
- langchain
- langchain community- text spiliter
- langchain core
- langchain hub - it helps to download prompts that are contributed by community


for using env created launch json file and added path of json there.

Prompt -> simple text which is given to the llm and then llm process it and give output
Prompt Templates -> llm receive as input something which is called prompt. It adds functionality to prompt to receive an input from user.

Chat models -> wrapper around llm that helps to interact with llm as we are in chat.

for using ollama model we have to use pipenv install langchain-ollama and use ChatOllama

Output parsers - output of models can be either strings or messages which can be in any format (eg JSON etc) so output parsers are
responsible for taking output of the model and then tranforming into usable form.