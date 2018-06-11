FROM python:3.6-alpine3.6  
EXPOSE 8081  
WORKDIR /app  
COPY ./app.py .  
COPY ./requirements.txt .  
RUN pip --no-cache-dir install -r requirements.txt  
  
ENTRYPOINT ["python3", "app.py"]  

