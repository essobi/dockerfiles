FROM centos:7  
LABEL maintainer="marco.miglierina@contentwise.tv"  
  
ARG GOSU_VERSION=1.10  
RUN yum -y --setopt=tsflags=nodocs update && \  
yum -y --setopt=tsflags=nodocs install \  
epel-release && \  
yum -y --setopt=tsflags=nodocs install \  
dpkg && \  
yum clean all  
  
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
&& rm -r /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu

