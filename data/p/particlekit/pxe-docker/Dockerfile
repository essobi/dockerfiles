FROM httpd  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
tftpd-hpa --no-install-recommends  
  
EXPOSE 80 69  
  
VOLUME ["/usr/local/apache2/htdocs","/var/lib/tftpboot"]  
  
ADD init.sh /  
  
CMD ["/init.sh"]  

