FROM node:6.3.1  
MAINTAINER fosorio | InterWare  
  
#EXPOSE 8080  
#EXPOSE 3000  
RUN mkdir -p /opt/app  
COPY . /opt/app  
RUN cd /opt/app && npm install --production  
  
WORKDIR /opt/app  
  
CMD ["npm","run", "prepare"]  

