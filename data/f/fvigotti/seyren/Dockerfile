FROM fvigotti/docker-fatjdk8  
  
RUN apt-get update -y && apt-get -y install npm nodejs-legacy nodejs && \  
npm install -g wait-for-mongo  
  
ADD https://github.com/scobal/seyren/releases/download/1.3.0/seyren-1.3.0.jar
/opt/seyren.jar  
ADD run-seyren.sh /usr/bin/run-seyren.sh  
RUN chmod +x /usr/bin/run-seyren.sh  
  
ENTRYPOINT ["/usr/bin/run-seyren.sh"]  
EXPOSE 8080  

