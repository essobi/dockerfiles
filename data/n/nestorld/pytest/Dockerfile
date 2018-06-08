FROM python:3.4.8-slim-jessie  
  
WORKDIR /app  
  
ADD . /app  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8200  
CMD ["python", "py_for_container_test.py"]  

