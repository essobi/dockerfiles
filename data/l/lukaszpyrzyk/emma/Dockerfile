FROM python:3.6.5-alpine3.7  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY /src .  
  
CMD [ "python", "./app.py" ]  

