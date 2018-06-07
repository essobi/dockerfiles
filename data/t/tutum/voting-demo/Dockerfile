FROM python:2.7-slim  
  
WORKDIR /app  
  
ADD requirements.txt /app/requirements.txt  
RUN pip install -r requirements.txt  
  
ADD . /app  
  
EXPOSE 80  
CMD ["python", "app.py"]  

