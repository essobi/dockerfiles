FROM debian:wheezy  
MAINTAINER Patrick Poulain <docker@m41l.me>  
RUN apt-get update  
RUN apt-get -y install wget  
RUN wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-
key add -  
RUN echo "deb http://packages.elasticsearch.org/logstash/1.4/debian stable
main" >> /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install logstash  
RUN apt-get -y autoremove  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
COPY ./conf/logstash/logstash.conf /etc/logstash/logstash.conf  
COPY ./conf/logstash/patterns/nginx /opt/logstash/patterns/nginx  
COPY ./conf/logstash/patterns/varnish /opt/logstash/patterns/varnish  
  
RUN mkdir -p /var/log/nginx  
RUN mkdir -p /var/log/varnish  
  
CMD [ "/opt/logstash/bin/logstash", "agent", "-f",
"/etc/logstash/logstash.conf"]

