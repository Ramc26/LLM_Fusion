import cohere
from dotenv import load_dotenv
import os
from dataclasses import  dataclass
# api_key = os.getenv("API_KEY_COHERE")
@dataclass
class ChatData:
    query:str # this is the question you asked
    ans:str # here is the main answer  from Cohere API
    explain: str # it gives additionl context
    url:str # citation that it took from

# print(api_key)

co = cohere.Client("ySKBtQZDJnLlHkspoPoSRkRwa4BjkM2bGdyUWAr2")

while True:
  print("\n\nBOT:How can I Help You?:")
  response = co.chat(
    message=input("\nYou:"),
    connectors=[{"id": "web-search"}]
  )
  

  data=ChatData(
      query=response.message,
      ans=response.text,
      explain=response.documents[0]['snippet'],
      url=response.documents[0]["url"]
  )

  print('#################################')
  print(f"QUESTION: {data.query}\n\nANSWER: {data.ans}\n\nCITATION: {data.url}")
  print('#################################')

  with open('output.txt', 'w') as file:
      file.write(str(response)+'\n')