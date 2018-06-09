FROM python:3.6-alpine3.6  
# Bundle app source  
RUN mkdir -p /var/app/mapd-service  
  
COPY . /var/app/mapd-service  
  
WORKDIR /var/app/mapd-service  
  
RUN pip install --no-cache-dir -r requirements.txt  
  
CMD ["python3", "app.py"]

