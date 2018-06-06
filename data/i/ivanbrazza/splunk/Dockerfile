FROM splunk/splunk  
  
ENV SPLUNK_ACCEPT_LICENSE false  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod +x /sbin/entrypoint.sh  
  
# Ports Splunk Web, Splunk Daemon, KVStore, Splunk Indexing Port, Network
Input, HTTP Event Collector  
EXPOSE 8000/tcp 8089/tcp 8191/tcp 9997/tcp 1514 8088/tcp  
  
WORKDIR /opt/splunk  
  
# Configurations folder, var folder for everything (indexes, logs, kvstore)  
VOLUME [ "/opt/splunk/etc", "/opt/splunk/var" ]  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["start-service"]

