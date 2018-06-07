FROM davidgaya/existdb:latest  
  
LABEL image.maintainer="Yannis Marketakis" \  
image.organization="FORTH-ICS" \  
image.version="2.2" \  
image.lastupdate="2017-10-04" \  
image.description="eXist-db image with 3M Resources"  
  
ADD entrypoint.sh /entrypoint.sh  
  
COPY Resources/3M /3M  
  
ADD Resources/data.tar.gz /opt/exist/webapp/WEB-INF/  
  
RUN sed -i 's/8080/8081/g' /opt/exist/tools/jetty/etc/jetty.xml \  
&& sed -i 's/8080/8081/g' /opt/exist/client.properties \  
&& sed -i 's/8080/8081/g' /opt/exist/backup.properties \  
&& sed -i 's/8080/8081/g' /opt/exist/index.html  
  
EXPOSE 8081  
VOLUME ["/opt/exist/webapp/WEB-INF/data/","/3M/"]  
  
CMD ["/entrypoint.sh"]  

