ARG DOCKER_VERSION=17.12  
FROM docker:${DOCKER_VERSION}  
  
ARG COMPOSE_VERSION=1.18.0  
  
RUN apk add \--no-cache python3  
RUN pip3 install --no-cache-dir docker-compose==${COMPOSE_VERSION}  

