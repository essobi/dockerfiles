FROM python:3.7.0b4-alpine3.7  
MAINTAINER Mopsalarm  
  
EXPOSE 8080  
COPY requirements.txt /app/requirements.txt  
RUN pip install --no-cache-dir -r /app/requirements.txt  
  
COPY . /app  
  
WORKDIR /app  
  
CMD ["python3", "-m", "bottle", "-s", "cherrypy", "-b", "0.0.0.0:8080",
"main"]  

