  
FROM ubuntu:16.04  
  
RUN apt-get update -y && apt-get install -y python-pip python-dev build-
essential  
RUN apt-get install -y git tesseract-ocr libpq-dev libssl-dev libffi-dev vim  
  
ADD . /usr/Coca-Cola  
  
RUN cd /usr/Coca-Cola && \  
pip install -r requirements.txt

