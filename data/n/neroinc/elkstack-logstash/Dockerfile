FROM logstash:1.5.4  
# Update and install additional plugins  
RUN /opt/logstash/bin/plugin update logstash-input-lumberjack logstash-input-
sqs logstash-output-http logstash-filter-mutate  
RUN /opt/logstash/bin/plugin install logstash-codec-cloudtrail  
RUN /opt/logstash/bin/plugin install logstash-codec-cloudfront  
RUN /opt/logstash/bin/plugin install logstash-input-cloudwatch  
RUN /opt/logstash/bin/plugin install logstash-filter-translate  
  
# Use custom entrypoint shell script  
COPY docker-entrypoint.sh /custom-entrypoint.sh  
RUN chmod +x /custom-entrypoint.sh  
ENTRYPOINT ["/custom-entrypoint.sh"]  
CMD ["logstash"]

