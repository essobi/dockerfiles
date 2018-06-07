FROM python:3-alpine  
MAINTAINER Denys Stroebel <z@stroebs.io>  
  
WORKDIR /app/  
  
COPY requirements.txt ./  
  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY src/ ./  
  
CMD ["python", "./main.py"]  

