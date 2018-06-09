FROM node:6  
MAINTAINER Vladimir Iakovlev <nvbn.rm@gmail.com>  
  
RUN adduser --disabled-password --gecos "" mrw-telegram  
WORKDIR /home/mrw-telegram  
USER mrw-telegram  
  
COPY . /home/mrw-telegram/  
USER root  
RUN chown -R mrw-telegram /home/mrw-telegram/  
RUN npm install  
USER mrw-telegram  
  
CMD npm start  

