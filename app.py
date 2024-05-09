from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
from langserve import add_routes
import uvicorn
from fastapi import FastAPI

load_dotenv()

app=FastAPI(
    title="Langchain Api",
    version='1.0',
    description="Uma api simples com Gemini"
)
model1=ChatOpenAI()
model=ChatGoogleGenerativeAI(model='gemini-pro')

prompt=ChatPromptTemplate.from_template('escreve um poema sobe {topico}')

add_routes(
    app,
    prompt|model,
    path='/gemini',
    playground_type='default'
)

if __name__=='__main__':
    uvicorn.run(app,host='localhost',port=8000)
    #uvicorn app:app --host 0.0.0.0 --port 9000