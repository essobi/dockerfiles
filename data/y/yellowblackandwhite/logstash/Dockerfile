FROM logstash:2.4  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
RUN cd /opt/logstash && \  
bin/plugin install logstash-output-lumberjack && \  
bin/plugin install logstash-input-lumberjack && \  
bin/plugin install logstash-output-http && \  
bin/plugin install logstash-input-http && \  
bin/plugin install logstash-output-elasticsearch && \  
bin/plugin install logstash-filter-elasticsearch && \  
bin/plugin install logstash-filter-translate && \  
bin/plugin install logstash-filter-date && \  
bin/plugin install logstash-filter-grok && \  
bin/plugin install logstash-filter-fingerprint && \  
bin/plugin install logstash-filter-anonymize && \  
bin/plugin install logstash-filter-mutate  

