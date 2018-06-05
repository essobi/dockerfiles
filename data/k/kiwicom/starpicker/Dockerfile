FROM python:3-slim  
  
MAINTAINER Simone Esposito <simone@kiwi.com>  
  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY requirements.txt /app/  
RUN pip install --no-cache-dir -r requirements.txt  
COPY . /app  
  
CMD [ "python", "-m", "starpicker.run" ]  

