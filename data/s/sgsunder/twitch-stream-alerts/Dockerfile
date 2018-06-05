FROM python:2.7.14-alpine  
  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY *.py ./  
  
ENTRYPOINT ["python", "./alert.py"]  

