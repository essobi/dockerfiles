FROM rabbitmq:3.6-management  
  
# Install ifconfig (for automatic registration in Consul) and curl (for
clustering).  
RUN apt-get update && apt-get install -y --no-install-recommends net-tools
curl jq && rm -rf /var/lib/apt/lists/*  
  
# Add custom entrypoint script.  
COPY command.sh /opt/command.sh  
RUN chmod +x /opt/command.sh  
ENTRYPOINT ["/opt/command.sh"]  
  
CMD ["rabbitmq-server"]  

