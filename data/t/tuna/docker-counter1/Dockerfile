FROM python:3.4  
RUN pip install flask redis  
COPY . /app  
WORKDIR /app  
  
EXPOSE 5000  
CMD ["python", "app.py"]  
  

