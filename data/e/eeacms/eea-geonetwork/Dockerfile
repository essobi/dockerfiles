FROM tomcat:8-jre8  
  
MAINTAINER michimau <mauro.michielon@eea.europa.eu>  
  
RUN apt-get -y update  
RUN apt-get -y install vim  
RUN wget http://files.titellus.net/geonetwork/eea/eea-catalogues-3.4.3.tar.gz
-O eea-catalogues.tar.gz  
  
RUN tar -xvzf eea-catalogues.tar.gz -C /  
  
RUN sed -i 's/port="8080"/port="8080" URIEncoding="UTF-8"/'
/usr/local/tomcat/conf/server.xml  
  
COPY jdbc.properties /jdbc.properties  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8080 8019 8009  

