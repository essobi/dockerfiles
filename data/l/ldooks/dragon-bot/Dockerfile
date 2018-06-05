FROM python:3.6.2-alpine3.6  
LABEL name="Dragon Bot"  
RUN apk update && apk add --no-cache docker  
  
RUN pip install requests discord.py docker pybooru wolframalpha  
ADD app /app  
  
CMD python app/dragon-bot.py

