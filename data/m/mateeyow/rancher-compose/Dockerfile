FROM gliderlabs/alpine:3.4  
  
MAINTAINER Matthew Torres <matthew.torres211@gmail.com>  
  
RUN apk-install openssl \  
&& wget https://github.com/rancher/rancher-
compose/releases/download/v0.8.3/rancher-compose-linux-amd64-v0.8.3.tar.gz \  
&& tar -zxvf rancher-compose-linux-amd64-v0.8.3.tar.gz \  
&& mv rancher-compose-v0.8.3/rancher-compose /bin/  
  
RUN rm -rf rancher-compose-v0.8.3 rancher-compose-linux-amd64-v0.8.3.tar.gz  
  
ENTRYPOINT ["/bin/rancher-compose"]

