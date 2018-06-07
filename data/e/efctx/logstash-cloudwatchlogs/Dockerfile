FROM logstash:2.3.4  
RUN apt-get update -qq && apt-get install -qqy git && rm -rf /var/cache/apt  
ADD . /build  
  
WORKDIR /opt/logstash  
RUN bin/logstash-plugin install /build/logstash-output-
cloudwatchlogs-2.0.0.pre1.gem  
RUN bin/logstash-plugin install logstash-filter-json_encode  
WORKDIR /  

