FROM debian:jessie  
  
RUN mkdir /gateway  
WORKDIR /gateway  
  
ADD gateway /gateway/gateway  
RUN chmod +x /gateway/gateway  
  
ENTRYPOINT ./gateway  

