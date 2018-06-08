FROM yatsecksch/alpine-java-8  
MAINTAINER yatseck <jacek.schoepe@ista.com>  
  
# Installing wget  
RUN apk --no-cache add openssl  
RUN apk update && \  
apk add ca-certificates && \  
update-ca-certificates  
RUN apk add wget  
  
# add tomcat version into image  
ADD http://ftp.ps.pl/pub/apache/tomcat/tomcat-7/v7.0.77/bin/apache-
tomcat-7.0.77.tar.gz /srv  
# decompress tomcat' file  
RUN tar xzvf /srv/apache-tomcat-7.0.77.tar.gz -C /srv/  
# change credentials for tomcat manager  
COPY tomcat-users.xml /srv/apache-tomcat-7.0.77/conf/tomcat-users.xml  
# Create the tomcat user and group  
RUN adduser tomcat -h /srv/apache-tomcat-7.0.77 -D  
RUN chown -R tomcat:tomcat /srv/apache-tomcat-7.0.77  
# set CATALINA_HOME  
ENV CATALINA_HOME /srv/apache-tomcat-7.0.77  
ENV PATH $CATALINA_HOME/bin:$PATH  
  
# set ports to be exposed outsied te container  
EXPOSE 8080 8009 8005  
# Run everything below as the tomcat user  
USER tomcat  
  
CMD ["catalina.sh", "run"]  

