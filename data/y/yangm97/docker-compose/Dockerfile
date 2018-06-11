FROM docker:latest  
WORKDIR /workdir  
RUN apk add --no-cache py-pip && pip install docker-compose  
ENTRYPOINT docker-compose  

