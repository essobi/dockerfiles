# Base image  
FROM progrium/consul  
  
# Add the configuration file  
ADD config/consul_config.json /config/consul_config.json  
  
ADD run.sh /opt/run.sh  
  
# Run consul  
ENTRYPOINT ["/opt/run.sh"]  

