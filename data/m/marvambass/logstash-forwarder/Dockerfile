FROM marvambass/oracle-java8  
  
RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
RUN echo 'deb http://packages.elasticsearch.org/logstashforwarder/debian
stable main' > /etc/apt/sources.list.d/logstashforwarder.list  
  
RUN apt-get update; apt-get install -y \  
logstash-forwarder  
  
ENV PATH /opt/logstash-forwarder/bin:$PATH  
  
COPY entrypoint.sh /  
  
VOLUME ["/logstash-forwarder-conf", "/certs"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["logstash-forwarder", "-config=/etc/logstash-forwarder.conf"]  

