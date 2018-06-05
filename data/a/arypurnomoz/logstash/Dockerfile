FROM arypurnomoz/java  
  
ENV VERSION 1.4.2  
ADD
https://download.elasticsearch.org/logstash/logstash/logstash-${VERSION}.zip
/tmp/logstash.zip  
  
WORKDIR /tmp  
  
RUN \  
unzip /tmp/logstash.zip \  
&& rm -f /tmp/logstash.zip \  
&& mv /tmp/logstash-* /logstash  
  
ADD run.sh /tmp/run.sh  
  
ENTRYPOINT ["/tmp/run.sh"]  

