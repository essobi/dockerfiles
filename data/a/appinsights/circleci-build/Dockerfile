FROM python:2-alpine  
  
ENV VER="17.05.0-ce"  
ENV COMPOSE_VER="1.13.0"  
  
RUN pip install flake8 awscli docker-compose && \  
apk add --no-cache ca-certificates wget curl git openssh && \  
update-ca-certificates  
  
RUN wget -O /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz && \  
mkdir -p /tmp/docker-bin/ && \  
tar -xz -C /tmp/docker-bin/ -f /tmp/docker-$VER.tgz && \  
mv /tmp/docker-bin/docker/* /usr/bin  
  

