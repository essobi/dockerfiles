FROM wizeye/n3n-base  
  
# Install wizeye proxy  
ADD wizeye-proxy.tar.gz /  
  
# Update the settings for wizeye proxy  
ADD run.sh /run.sh  
  
RUN chmod +x /run.sh  
  
EXPOSE 8090  
CMD ["/bin/sh", "-c", "/run.sh"]  

