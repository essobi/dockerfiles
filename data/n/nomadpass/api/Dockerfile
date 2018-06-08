FROM python:alpine  
  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY . /app  
  
RUN pip install -r requirements.txt  
  
CMD ["python", "api.py"]  

