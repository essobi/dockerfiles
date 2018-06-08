FROM vikrantj/java:8u91  
  
MAINTAINER Vikrant Jain <vikrantj.develop@gmail.com>  
  
ARG LOGSTASH_VERSION=1.5.4  
ARG
LOGSTASH_URL=https://download.elastic.co/logstash/logstash/logstash-${LOGSTASH_VERSION}.tar.gz  
  
RUN curl -SL ${LOGSTASH_URL} -o /logstash.tar.gz \  
&& tar zxf /logstash.tar.gz \  
&& mv /logstash-${LOGSTASH_VERSION} /logstash \  
&& rm -rf logstash.tar.gz \  
&& /logstash/bin/plugin install logstash-output-websocket  
  
ENTRYPOINT ["/logstash/bin/logstash"]  

