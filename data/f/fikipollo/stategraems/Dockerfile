############################################################  
# Dockerfile to build STATegra EMS container images  
# Based on tomcat  
############################################################  
  
# Set the base image to official Tomcat  
FROM tomcat  
  
# File Author / Maintainer  
MAINTAINER Rafa Hernandez <https://github.com/fikipollo>  
  
################## BEGIN INSTALLATION ######################  
# Install MySQL client for connecting to the MySQL component  
RUN apt-get update && apt-get install -y mysql-client  
  
# Download the lastest image of STATegra EMS  
RUN wget -O /tmp/stategraems.zip
https://github.com/fikipollo/stategraems/archive/v0.9.zip \  
&& unzip /tmp/stategraems.zip -d /tmp/stategraems \  
&& cp /tmp/stategraems/*/dist/stategraems.war /usr/local/tomcat/webapps/ \  
&& rm -r /tmp/stategraems \  
&& rm -r /tmp/stategraems.zip \  
&& sleep 10 \  
&& rm -r /usr/local/tomcat/webapps/ROOT \  
&& ln -s /usr/local/tomcat/webapps/stategraems /usr/local/tomcat/webapps/ROOT
\  
&& echo "export is_docker=true" >> /usr/local/tomcat/bin/setenv.sh \  
&& chmod +x /usr/local/tomcat/bin/setenv.sh  
  
##################### INSTALLATION END #####################  
  
# Mark folders as imported from the host.  
VOLUME ["/data/"]  

