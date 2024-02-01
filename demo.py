import os
from salesgpt.agents import SalesGPT
import litellm

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env") # replace "path/to/.env" with the actual path to your .env file

# select your model - Gemini
llm = litellm(temperature=0.4, model_name="gemini-pro")

sales_agent = SalesGPT.from_llm(llm, use_tools=True, verbose=False,
              product_catalog = "sample_product_catalog.txt",
              salesperson_name="Ted Lasso",
              salesperson_role="Sales Representative",
              company_name="Sleep Haven",
              company_business='''Sleep Haven 
              is a premium mattress company that provides
              customers with the most comfortable and
              supportive sleeping experience possible. 
              We offer a range of high-quality mattresses,
              pillows, and bedding accessories 
              that are designed to meet the unique 
              needs of our customers.'''
              )
sales_agent.seed_agent()
sales_agent.determine_conversation_stage() # optional for demonstration, built into the prompt
# agent 
sales_agent.step()

# user
user_input = input('Your response: ') # Yea, sure
sales_agent.human_step(user_input)

# agent
sales_agent.determine_conversation_stage() # optional for demonstration, built into the prompt
sales_agent.step()

# user
user_input = input('Your response: ') # What pricing do you have for your mattresses?
sales_agent.human_step(user_input)

# agent
sales_agent.determine_conversation_stage() # optional for demonstration, built into the prompt
sales_agent.step()