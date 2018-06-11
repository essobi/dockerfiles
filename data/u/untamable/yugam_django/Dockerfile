FROM python:2.7  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
RUN apt-get update  
RUN apt-get -y install pdftk  
COPY requirements.txt /usr/src/app/  
COPY extras/ /root/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  

