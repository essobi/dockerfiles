FROM python:3.6-alpine  
  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
ENV PYTHONPATH /app/  
  
COPY . .  
  
CMD ["huey_consumer", "checker.huey"]

