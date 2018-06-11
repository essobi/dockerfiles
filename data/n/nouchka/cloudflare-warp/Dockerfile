FROM debian  
  
RUN apt-get update && apt-get install -y wget  
RUN wget -O- https://bin.equinox.io/c/2ovkwS9YHaP/edgetunnels-stable-linux-
amd64.tgz | tar xz  
  
ENV DOMAIN ggt.example.com  
  
COPY start.sh /cloudflare-start  
  
RUN chmod +x /cloudflare-start  
  
ENTRYPOINT ["/cloudflare-start"]  

