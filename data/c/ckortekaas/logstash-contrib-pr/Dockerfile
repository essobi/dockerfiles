FROM ckortekaas/logstash-contrib  
MAINTAINER Christiaan Kortekaas <mrangryfish@gmail.com>  
  
#So far we are only working with a single pull request to improve the ES
filter so this is the simplest way to get it  
#Hopefully it will be pulled into the official logstash-contrib and this won't
be needed over time  
RUN cd /tmp && \  
wget https://raw.githubusercontent.com/ckortekaas/logstash-
contrib/master/lib/logstash/filters/elasticsearch.rb && \  
mv elasticsearch.rb /opt/logstash/lib/logstash/filters/.

