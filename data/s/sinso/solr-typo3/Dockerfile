FROM java:6-jre  
MAINTAINER Jonas Renggli <jonas.renggli@swisscom.com>  
  
ADD assets/install-solr.sh /install-solr.sh  
  
RUN /install-solr.sh english german french italian  
  
ADD assets/solr.xml /opt/solr-tomcat/solr/solr.xml  
ADD assets/server.xml /opt/solr-tomcat/tomcat/conf/server.xml  
  
EXPOSE 8080  
#ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/opt/solr-tomcat/tomcat/bin/catalina.sh", "run"]  

