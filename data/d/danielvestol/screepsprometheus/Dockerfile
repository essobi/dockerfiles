FROM node:latest  
RUN apt-get update && apt install git -y  
  
RUN git clone https://github.com/Danielv123/screepsPrometheus.git && cd
screepsPrometheus && npm install  
  
WORKDIR screepsPrometheus  
LABEL maintainer "danielv@live.no"  
EXPOSE 8081  
VOLUME /screepsPrometheus/config  
  
CMD git pull && node index.js  

