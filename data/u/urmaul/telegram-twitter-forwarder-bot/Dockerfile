FROM python:3-alpine  
  
COPY requirements.txt /  
  
RUN pip3 install -r /requirements.txt  
  
ENV TELEGRAM_BOT_TOKEN=  
ENV TWITTER_CONSUMER_KEY=  
ENV TWITTER_CONSUMER_SECRET=  
# optionally  
ENV TWITTER_ACCESS_TOKEN=  
ENV TWITTER_ACCESS_TOKEN_SECRET=  
  
RUN mkdir /app  
COPY *.py /app/  
  
WORKDIR /app  
CMD python3 /app/main.py  

