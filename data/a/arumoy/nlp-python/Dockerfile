FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y software-properties-common && add-
apt-repository -y ppa:alex-p/tesseract-ocr  
RUN apt-get update && apt-get install -y tesseract-ocr  
  
RUN mkdir /home/work  
WORKDIR /home/work  
  
RUN apt-get update  
RUN apt-get install python3-pip -y  
RUN pip3 install --upgrade pip  
RUN pip3 install requests  
RUN pip3 install pillow  
RUN pip3 install numpy  
RUN pip3 install sklearn  
RUN pip3 install pandas  
RUN pip3 install pytesseract  
RUN pip3 install scipy  
RUN pip3 install nltk

