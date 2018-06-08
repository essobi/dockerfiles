FROM python:3.6-alpine3.6  
WORKDIR /app  
  
COPY . /app  
  
RUN pip install -r requirements.txt  
  
EXPOSE 5000  
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5000", "api.main:app"]  

