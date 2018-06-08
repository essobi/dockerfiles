FROM docker:1.13-dind  
MAINTAINER Alexei Ledenev <alexei.led@gmail.com>  
  
ENV COMPOSE_VER=1.11.2  
ENV DOBI_VER=v0.9  
# install useful tools  
RUN apk --no-cache add \  
git \  
openssl \  
openssh-client \  
ca-certificates \  
curl \  
wget \  
bash \  
jq \  
vim  
  
# install dobi - Docker build automation for Docker  
RUN curl -L
https://github.com/dnephin/dobi/releases/download/${DOBI_VER}/dobi-linux >
/usr/local/bin/dobi && \  
chmod +x /usr/local/bin/dobi  
  
# install docker-compose  
RUN curl -L
https://github.com/docker/compose/releases/download/${COMPOSE_VER}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
# Add files for CF node registration  
RUN mkdir -p /cf  
COPY register.json register_cf_node.sh services-kv.sh /cf/  

