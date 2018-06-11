FROM node  
LABEL com.aerohive.keyservice.version="0.1"  
LABEL com.aerohive.keyservice.release-date="2017-10-11"  
  
RUN npm install -g bower  
  
COPY ./src /app/  
  
WORKDIR /app  
  
RUN npm install && bower install --allow-root  
  
RUN groupadd -r ah && useradd -mr -g ah ah  
USER ah  
  
EXPOSE 51360  
ENTRYPOINT /app/docker-entrypoint.sh 51360  
  

