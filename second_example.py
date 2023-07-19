import openai
import os
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import ChatPromptTemplate

_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

def get_completion(prompt,model='gpt-3.5-turbo'):
   messages = [{"role":"user","content":prompt}]
   response = openai.ChatCompletion.create(
      model=model,
      messages=messages,
      temperature=0
   )
   return response.choices[0].message["content"]



# customer email in english pirates language
customer_email = """
Arrr, I be fuming that  me blender lid flew off and splattered me kitchen walls with smoothie! And to make matters worse,the warranty don't cover the cost of cleaning up me kitchen. I need yer help right now, matey!
"""

style = """
American English in a calm and respectful tone
"""

prompt = f"""
Translate the text that is delimited by triple backticks into  a style that is {style}. text : ```{customer_email}```
"""

response = get_completion(prompt)

response

