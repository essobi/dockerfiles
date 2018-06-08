FROM mysql:5.7  
MAINTAINER Emanuel Righetto <posta@emanuelrighetto.it>  
  
# Add MySQL scripts  
COPY workaround_permissions.sh /workaround_permissions.sh  
RUN chmod +x /workaround_permissions.sh  
  
CMD ["/workaround_permissions.sh"]  

