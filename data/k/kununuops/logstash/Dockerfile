  
FROM micwevermind/docker-logstash-filter-tester:6.2.2  
  
ADD pipelines /pipelines  
RUN bin/rspec --force-color /pipelines/main/filter_tests.rb  
  
FROM docker.elastic.co/logstash/logstash-oss:6.2.2  
  
# See https://www.elastic.co/guide/en/logstash/current/plugins-outputs-
elasticsearch.html#_dns_caching  
ENV LS_JAVA_OPTS="-Dnetworkaddress.cache.ttl=1"  
ADD pipelines.yml /usr/share/logstash/config/pipelines.yml  
ADD pipelines /usr/share/logstash/pipelines  
ADD update_config.py /usr/share/logstash/update_config.py  
ADD entrypoint.sh /usr/share/logstash/entrypoint.sh  
USER root  
RUN chown -R logstash:logstash /usr/share/logstash/config/pipelines.yml
/usr/share/logstash/pipelines  
USER logstash  
  
ENTRYPOINT /usr/share/logstash/entrypoint.sh  

