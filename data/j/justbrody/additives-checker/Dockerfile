  
FROM ubuntu:18.04  
RUN apt-get update && apt-get install -y software-properties-common && add-
apt-repository -y ppa:alex-p/tesseract-ocr  
RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-nld  
RUN apt-get install -y imagemagick  
RUN apt-get install nodejs -y  
RUN apt-get install npm -y  
RUN apt-get install exiftran -y  
  
WORKDIR /usr/src/app  
  
COPY package*.json ./  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  
  

