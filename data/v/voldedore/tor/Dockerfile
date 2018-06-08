FROM alpine:latest  
  
  
RUN apk update; \  
apk add tor  
  
RUN echo 'SocksPort 0.0.0.0:9050 IsolateDestAddr' >> /etc/tor/torrc  
  
EXPOSE 9050  
CMD tor  
  

