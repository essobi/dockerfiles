FROM little78926/debian-nodejs-s3fs  
  
RUN apt-get update  
  
# Chinese Font  
RUN apt-get install -y fonts-noto fonts-arphic-ukai fonts-arphic-uming  
RUN apt-get install -y ttf-wqy-microhei ttf-wqy-zenhei  
  
ARG local="."  
WORKDIR /application  
RUN mkdir -p /application  
  
COPY $local/package.json /application  
RUN npm i  
RUN npm i pm2 -g  
  
COPY $local /application  
RUN npm run build  
  
RUN chmod +x /application/DockerRun.sh  
  
EXPOSE 8080  
ENTRYPOINT ["/application/DockerRun.sh"]  

