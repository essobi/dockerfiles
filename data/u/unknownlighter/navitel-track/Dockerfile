FROM python:3.5-alpine  
  
ADD requirements.txt .  
  
RUN pip install -r requirements.txt  
  
ADD server.py .  
  
EXPOSE 80  
CMD ./server.py  

