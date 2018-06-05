FROM docker.elastic.co/logstash/logstash:6.1.1  
RUN bin/logstash-plugin install logstash-output-solr_http  
RUN sed -i 's/iso8601/to_iso8601/g'
/usr/share/logstash/vendor/bundle/jruby/2.3.0/gems/logstash-output-
solr_http-3.0.4/lib/logstash/outputs/solr_http.rb  
  
RUN bin/logstash-plugin install logstash-input-beats  
RUN bin/logstash-plugin install logstash-filter-multiline

