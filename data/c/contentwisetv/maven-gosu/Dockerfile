FROM maven:3.5.3-jdk-8  
ARG GOSU_VERSION=1.10  
RUN apt-get update && apt-get install -y \  
build-essential \  
libxml2-utils && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN for server in ha.pool.sks-keyservers.net \  
hkp://p80.pool.sks-keyservers.net:80 \  
keyserver.ubuntu.com \  
hkp://keyserver.ubuntu.com:80 \  
pgp.mit.edu; \  
do \  
gpg --keyserver "$server" \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && break || echo "Trying new
server..."; \  
done  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu

