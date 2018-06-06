# Deploy builds to a Rancher orchestrated stack using rancher-compose  
#  
# docker build --rm=true -t dangerfarms/drone-rancher .  
FROM gliderlabs/alpine:3.2  
MAINTAINER Lewis Taylor <lewis@dangerfarms.com>  
  
ENV VERSION=1.0.0  
ENV RANCHER_COMPOSE_VERSION=0.12.1  
RUN mkdir -p /opt/drone  
WORKDIR /opt/drone  
  
RUN apk-install openssl ca-certificates && \  
wget -O rancher-compose.tar.gz https://github.com/rancher/rancher-
compose/releases/download/v$RANCHER_COMPOSE_VERSION/rancher-compose-linux-
amd64-v$RANCHER_COMPOSE_VERSION.tar.gz && \  
tar -zxvf rancher-compose.tar.gz && \  
mv ./rancher-compose-v$RANCHER_COMPOSE_VERSION/rancher-compose /usr/bin/ && \  
rm -rf rancher-compose*  
  
RUN apk-install python3  
  
COPY requirements.txt /opt/drone/  
RUN pip3 install -r requirements.txt  
COPY main.py /opt/drone/  
  
ENTRYPOINT ["python3", "/opt/drone/main.py"]  

