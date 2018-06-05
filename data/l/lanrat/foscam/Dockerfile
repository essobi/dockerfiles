FROM node  
  
WORKDIR /app  
RUN apt-get update  
RUN apt-get install -y git libav-tools  
RUN git clone https://github.com/phoboslab/jsmpeg.git  
  
COPY package.json /app/package.json  
RUN npm install  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 8084  
CMD ["/docker-entrypoint.sh"]

