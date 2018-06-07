FROM alpine:3.6  
MAINTAINER bloomandwild  
  
VOLUME /app  
WORKDIR /app  
  
RUN apk --no-cache add ca-certificates openssl && update-ca-certificates  
  
RUN cd /tmp && \  
wget https://github.com/rancher/rancher-
compose/releases/download/v0.12.5/rancher-compose-linux-amd64-v0.12.5.tar.gz
&& \  
tar zxvf rancher-compose-linux-amd64-v0.12.5.tar.gz && \  
mv rancher-compose-v0.12.5/rancher-compose /usr/local/bin/ && \  
chmod 755 /usr/local/bin/rancher-compose && \  
rm -rf /tmp/rancher-compose-v0.12.5  
  
ENTRYPOINT ["/usr/local/bin/rancher-compose"]  

