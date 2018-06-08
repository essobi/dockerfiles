FROM httpd:2.2  
MAINTAINER NutsProject,LLC  
  
RUN tar czf /usr/src/apache2-default-doc.tar.gz -C /usr/local/apache2/htdocs
./ \  
&& tar czf /usr/src/apache2-conf.tar.gz -C /usr/local/apache2/conf ./  
  
WORKDIR /usr/local/apache2/htdocs  
  
COPY docker-entrypoint-ex.sh /entrypoint-ex.sh  
  
ENTRYPOINT ["/entrypoint-ex.sh"]  

