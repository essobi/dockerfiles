FROM java:8-jre  
  
ADD ./logstash.conf /etc/logstash/logstash.conf  
  
ENV LOGSTASH_VERSION 1.5.0.beta1  
RUN curl -s
"https://download.elasticsearch.org/logstash/logstash/logstash-${LOGSTASH_VERSION}.tar.gz"
| \  
tar xz -C /opt && \  
mv "/opt/logstash-${LOGSTASH_VERSION}" /opt/logstash  
  
ENTRYPOINT ["/opt/logstash/bin/logstash"]  
CMD ["-f", "/etc/logstash/logstash.conf"]  

