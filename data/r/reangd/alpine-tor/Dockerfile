FROM reangd/alpine-base:latest  
  
RUN apk add --no-cache tor && \  
echo SOCKSPort 0.0.0.0:9050 > /etc/tor/torrc  
  
EXPOSE 9050  
COPY root /  

