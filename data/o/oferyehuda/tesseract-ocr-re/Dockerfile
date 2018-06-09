  
# Tesseract 4 OCR Runtime Environment - Docker Container  
#  
FROM ubuntu:16.04  
  
RUN apt-get update && apt-get install -y software-properties-common && add-
apt-repository -y ppa:alex-p/tesseract-ocr  
RUN apt-get update && apt-get install -y tesseract-ocr  
RUN apt-get install -y python3-requests  
RUN apt-get install -y python3-pip python-dev build-essential  
RUN apt-get install -y python-imaging  
RUN pip3 install --upgrade pip setuptools; pip3 install Flask  
  
EXPOSE 8080  
WORKDIR /ocr  
cmd FLASK_APP=ocr/web_app.py flask run \--host=0.0.0.0 \--port=8080  

