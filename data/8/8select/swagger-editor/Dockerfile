FROM node:5  
  
RUN apt-get update && \  
apt-get install unzip && \  
apt-get clean && \  
wget https://github.com/swagger-api/swagger-
editor/releases/download/v2.9.8/swagger-editor.zip && \  
unzip swagger-editor.zip && \  
npm cache clean && \  
npm install -g http-server && \  
npm cache clean  
  
CMD ["http-server", "swagger-editor"]  

