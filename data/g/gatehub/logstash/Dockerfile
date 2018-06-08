FROM logstash:5.6.8  
ADD https://rubygems.org/downloads/logstash-output-influxdb-5.0.4.gem
/logstash-output-influxdb.gem  
RUN logstash-plugin install /logstash-output-influxdb.gem  
  
ADD https://rubygems.org/downloads/logstash-filter-kubernetes-0.3.1.gem
/logstash-filter-kubernetes.gem  
RUN logstash-plugin install /logstash-filter-kubernetes.gem  

