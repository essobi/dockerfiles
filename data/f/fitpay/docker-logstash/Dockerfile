FROM fitpay/docker-java  
  
RUN rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch  
ADD logstash.repo /etc/yum.repos.d/logstash.repo  
  
RUN yum install -y logstash  
RUN /opt/logstash/bin/logstash-plugin install logstash-input-beats  
  
RUN mkdir -p /app/bin  
RUN mkdir -p /etc/fitpay/conf  
ADD conf/logstash.conf /etc/fitpay/conf/logstash.conf  
  
ADD bin/logstash /app/bin/logstash  
  
CMD ["/app/bin/logstash"]  

