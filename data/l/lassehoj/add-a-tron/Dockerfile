FROM python:2.7-alpine3.7  
COPY requirements.txt /  
  
RUN pip install -r requirements.txt  
  
COPY addition.py /  
  
CMD ["python", "addition.py"]  

