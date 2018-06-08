FROM docker.elastic.co/logstash/logstash:5.6.3  
  
COPY logstash-output-dynamodb-0.0.1.gem /tmp/  
#COPY logstash-output-dynamodb.gemspec /tmp/  
  
#RUN ls /tmp  
  
ENV PATH /opt/logstash/vendor/jruby/bin/:$PATH  
#RUN gem build /tmp/logstash-output-dynamodb.gemspec  
#RUN gem install /tmp/logstash-output-dynamodb-0.0.1.gem logstash-output-
dynamodb-0.0.1  
RUN /usr/share/logstash/bin/logstash-plugin install /tmp/logstash-output-
dynamodb-0.0.1.gem  
#RUN /usr/share/logstash/bin/logstash-plugin list  
  
  
#RUN gem install logstash-output-mongodb:3.1.3 logstash-output-mongodb:3.1.3  
#RUN gem install logstash-input-dynamodb:'> 2' logstash-filter-dynamodb:'> 2'  
#RUN plugin install logstash-input-dynamodb logstash-filter-dynamodb  
  
RUN rm -f /usr/share/logstash/pipeline/logstash.conf  
  
COPY ./config-dir/logstash.conf /usr/share/logstash/pipeline/logstash.conf  
COPY ./config-dir/aws.conf /usr/share/logstash/pipeline/aws.conf  
  
EXPOSE 9998  
#CMD ["/usr/share/logstash/bin/logstash-plugin", "list"]  
  
CMD ["-f", "/usr/share/logstash/pipeline/logstash.conf"]  

