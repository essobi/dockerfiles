FROM zingsono/centos:7  
MAINTAINER Zengs.<zingsono@gmail.com>  
LABEL Description="FORM centos:7 . logstash"  
  
WORKDIR /logstash  
  
ENV LOGSTASH_VERSION=6.2.4  
RUN curl -o logstash.tar.gz
"https://artifacts.elastic.co/downloads/logstash/logstash-$LOGSTASH_VERSION.tar.gz"
&& tar -xf logstash.tar.gz --strip-components=1 && rm -f logstash.tar.gz  
ENV PATH=$PATH:/logstash/bin/  
  
CMD ["logstash"]

