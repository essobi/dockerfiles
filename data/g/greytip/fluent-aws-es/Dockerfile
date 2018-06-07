FROM organizeme/docker-fluentd-elasticsearch-aws  
  
RUN /usr/sbin/td-agent-gem install fluent-plugin-docker_metadata_filter  
  
COPY plugin/fluent-aws-metadata.rb /etc/td-agent/plugin/fluent-aws-metadata.rb  
COPY td-agent.conf /etc/td-agent/td-agent.conf  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Create fluentd index template & run the Fluentd service.  
CMD ["/start.sh"]  
  

