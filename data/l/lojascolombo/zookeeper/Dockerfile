FROM openjdk:8-jre-alpine  
MAINTAINER Lojas Colombo "projetos-site@colombo.com.br"  
ENV ZOOKEEPER_VERSION "3.4.9"  
ENV ZOOKEEPER_RELEASE zookeeper-${ZOOKEEPER_VERSION}  
ENV ZOOKEEPER_URL_DOWNLOAD
https://archive.apache.org/dist/zookeeper/${ZOOKEEPER_RELEASE}/${ZOOKEEPER_RELEASE}.tar.gz  
  
RUN apk add --update bash unzip wget \  
&& wget -q "${ZOOKEEPER_URL_DOWNLOAD}" -O "/tmp/${ZOOKEEPER_RELEASE}.tar.gz" \  
&& tar xfz /tmp/${ZOOKEEPER_RELEASE}.tar.gz -C /tmp \  
&& mkdir -p /opt \  
&& mv /tmp/${ZOOKEEPER_RELEASE} /opt/zookeeper \  
&& rm /tmp/${ZOOKEEPER_RELEASE}.tar.gz \  
&& apk del unzip wget \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /opt/zookeeper/data  
  
ADD start-zookeeper.sh /opt/zookeeper/bin/start-zookeeper.sh  
  
VOLUME /opt/zookeeper/data  
WORKDIR /opt/zookeeper  
  
CMD /opt/zookeeper/bin/start-zookeeper.sh  

