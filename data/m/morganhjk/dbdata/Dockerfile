FROM busybox:latest  
  
# Prepare directories  
RUN mkdir -p /etc/mysql  
RUN mkdir -p /var/lib/mysql  
  
# Create volumes for mysql config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
# Run shell  
CMD ["/bin/sh"]  

