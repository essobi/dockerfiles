# Custom SOLR 4.x container  
FROM debian:jessie  
  
MAINTAINER Wim Vandersmissen <wim.vandersmissen@nascom.be>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SOLR_VERSION 4.10.4  
ENV SOLR solr-$SOLR_VERSION  
ENV SOLR_USER solr  
ENV SOLR_HOME /var/solr  
  
# Install SOLR  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
locales \  
unzip \  
openjdk-7-jre \  
&& wget --progress=bar:force
https://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz -O
/tmp/$SOLR.tgz \  
&& mkdir -p /usr/local/solr \  
&& tar xvf /tmp/$SOLR.tgz -C /usr/local/solr --strip-components 1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set UTF-8 locale  
RUN locale-gen nl_BE.UTF-8 && \  
echo 'LANG="nl_BE.UTF-8"' > /etc/default/locale  
  
# Set timezone  
RUN echo Europe/Brussels > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
RUN groupadd -g 3002 $SOLR_USER \  
&& useradd -u 3002 -d /opt/solr -s /sbin/false -g $SOLR_USER -G users
$SOLR_USER  
  
RUN mkdir -p $SOLR_HOME \  
&& mkdir -p $SOLR_HOME/logs \  
&& chown -R $SOLR_USER:$SOLR_USER $SOLR_HOME \  
&& chown -R $SOLR_USER:$SOLR_USER /usr/local/solr  
  
ADD ./config /config  
  
USER $SOLR_USER  
EXPOSE 8983  
COPY ./config/log4j.properties
/usr/local/solr/example/resources/log4j.properties  
COPY ./run.sh /run.sh  
COPY ./create_core.sh /create_core.sh  
  
ENTRYPOINT ["/run.sh"]  

