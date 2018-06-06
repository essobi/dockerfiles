FROM node:alpine  
  
COPY ./app /app  
  
RUN chmod +x /app/docker-entrypoint.sh  
  
WORKDIR /app  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"];

