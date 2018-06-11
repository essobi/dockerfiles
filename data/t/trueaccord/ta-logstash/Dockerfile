FROM logstash:1.5.3  
  
RUN /opt/logstash/bin/plugin install --version=0.1.6 logstash-output-
google_bigquery  
  
ADD https://raw.githubusercontent.com/thesamet/logstash-output-
google_bigquery/2ed062a405c512249b52d13783d30d2e9d58439e/lib/logstash/outputs/google_bigquery.rb
/opt/logstash/vendor/bundle/jruby/1.9/gems/logstash-output-
google_bigquery-0.1.6/lib/logstash/outputs/google_bigquery.rb  

