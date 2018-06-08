FROM alpine  
  
COPY gnatsd /gnatsd  
COPY entrypoint.sh /entrypoint.sh  
  
# Expose client, management, and cluster ports  
EXPOSE 4222 8222 6222  
# Run via the configuration file  
ENTRYPOINT ["/entrypoint.sh"]  

