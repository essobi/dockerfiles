FROM docker:18.04  
RUN apk update && \  
apk add --no-cache make bash python3 && \  
pip3 install docker-compose && \  
apk del python3  
  
CMD [ "docker-compose", "version" ]

