FROM python:3.6  
RUN apt-get update  
RUN apt-get -y install unzip  
  
#FROM python:3.6-alpine  
#  
#RUN apk update  
#RUN apk add unzip  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY ./data_provider ./data_provider  
COPY ./runner ./runner  
  
ENV PYTHONPATH /usr/src/app  
  
CMD [ "python", "./runner/main.py", "app", "./params.json" ]

