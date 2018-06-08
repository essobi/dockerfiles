FROM phusion/baseimage:0.9.18  
MAINTAINER Wynand Meintjes <wynand@responsive.co.za>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV FILEBEAT_VERSION=5.0.0-alpha2  
  
RUN apt-get update  
RUN apt-get install wget -y  
RUN wget -O /tmp/filebeat.tar.gz
https://download.elastic.co/beats/filebeat/filebeat-5.0.0-alpha2-x86_64.tar.gz  
RUN cd /tmp && tar xzvf filebeat.tar.gz \  
&& cd filebeat-* && cp filebeat /usr/local/bin/ \  
&& chmod +x /usr/local/bin/filebeat  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY config/filebeat.yml /  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]

