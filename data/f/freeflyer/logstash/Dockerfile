FROM java:8u92-jre-alpine  
  
MAINTAINER docker.com@xoop.org  
  
RUN apk -U add bash  
  
ENV LOGSTASH_VERSION 5.3.0  
ADD
https://artifacts.elastic.co/downloads/logstash/logstash-$LOGSTASH_VERSION.tar.gz
/tmp/ls.tgz  
  
RUN cd /usr/share && \  
tar xf /tmp/ls.tgz && \  
rm /tmp/ls.tgz  
  
WORKDIR /usr/share/logstash-$LOGSTASH_VERSION  
  
# For collectd reception  
EXPOSE 25826  
# /conf is the default directory where our logstash will read pipeline config
files  
# /logs is an optional attach point to reference something like /var/log on
the host  
VOLUME ["/conf","/logs"]  
  
ENV PLUGIN_UPDATES 2015-06-10  
RUN bin/logstash-plugin install logstash-input-heartbeat  
RUN bin/logstash-plugin install logstash-input-gelf  
#RUN bin/logstash-plugin install logstash-output-elasticsearch_groom  
RUN bin/logstash-plugin install logstash-output-elasticsearch  
  
CMD ["bin/logstash","-f","/conf"]  

