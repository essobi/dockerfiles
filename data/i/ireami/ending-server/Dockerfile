FROM postgres:9.6.5  
  
# This image is a version of the EDI-NG-Client Docker image  
  
MAINTAINER IREA <developers.mi@irea.cnr.it>  
  
# Install netcat, used in the tomcat-bin based script used to check the
database  
# is up and accepting connections before starting the 52North webapp.  
  
#RUN apk add --update \  
# netcat-openbsd \  
# curl \  
# unzip \  
# && rm -rf /var/cache/apk/*  
  
# Set the working directory and copy all the configuration files to the image.  
#WORKDIR /tmp  
#COPY rest-api-config/ rest-api-config/  
#COPY tomcat-conf/ tomcat-conf/  
#COPY sos-config/ sos-config/  
#COPY tomcat-bin/ tomcat-bin/  
  
# Copy the database connection checking script and set its permissions.  
#COPY tomcat-bin/* $CATALINA_HOME/bin  
#RUN chmod +x $CATALINA_HOME/bin/*.sh  
  
# Remove some of the WAR files  
#RUN rm -r $CATALINA_HOME/webapps/docs  
#RUN rm -r $CATALINA_HOME/webapps/examples  

