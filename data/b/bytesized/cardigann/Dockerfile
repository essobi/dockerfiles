FROM bytesized/debian-base  
MAINTAINER maran@bytesized-hosting.com  
  
RUN apt-get update && apt-get install -y wget  
RUN mkdir /app && \  
wget -O /app/cardigann.tgz https://bin.equinox.io/c/KpnfWEqtsi/cardigann-edge-
linux-amd64.tgz && \  
cd /app && tar -xvf /app/cardigann.tgz  
  
VOLUME /config  
  
COPY /static /  
  
EXPOSE 5060  

