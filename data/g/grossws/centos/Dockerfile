FROM centos:7  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
ARG GOSU_VERSION=1.10  
ARG
GOSU_URL=https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-
amd64  
  
RUN gpg -k &> /dev/null \  
&& echo 'keyid-format long' >> /root/.gnupg/gpg.conf \  
&& gpg --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -sSL $GOSU_URL -o /bin/gosu \  
&& chmod +x /bin/gosu \  
&& curl -sSL $GOSU_URL.asc -o /tmp/gosu.asc \  
&& gpg --verify /tmp/gosu.asc /bin/gosu \  
&& rm /tmp/gosu.asc  
  
RUN yum -y update \  
&& yum -y install tar \  
&& yum clean all \  
&& rm -rf /var/cache/yum \  
&& localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& localedef -i ru_RU -f UTF-8 ru_RU.UTF-8 \  
&& localedef -i ru_RU -f CP1251 ru_RU.CP1251  
  
ENV LANG en_US.UTF-8  

