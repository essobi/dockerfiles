FROM python:latest  
RUN apt-get update  
  
RUN mkdir /app  
VOLUME /app  
WORKDIR /app  
  
RUN pip install botogram  
RUN pip install pymongo  
RUN pip install requests  
RUN pip install celery  
RUN pip install redis  
RUN pip install celery[redis]  
  
CMD python /app/bot.py  

