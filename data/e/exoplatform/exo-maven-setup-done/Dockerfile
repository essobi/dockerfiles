FROM exoplatform/exo-maven  
MAINTAINER Nam Phung <namph@exoplatform.com>  
  
ENV TOMCAT_HOME /opt/exo/platform-community-4.1.0  
ENV ADM_LOG_DIR ${TOMCAT_HOME}/logs  
  
RUN cd $TOMCAT_HOME/gatein/conf/ && \  
mv exo-sample.properties exo.properties && \  
sed -i 's/#exo.accountsetup.skip=false/exo.accountsetup.skip=true/g'
exo.properties  
  
# Configuration for default users  
RUN cd $TOMCAT_HOME/gatein/conf/ && \  
mkdir portal && cd portal && mkdir portal && cd portal && \  
curl -L -o configuration.xml https://raw.githubusercontent.com/exo-docker/exo-
maven/master/exo-maven-setup-done/configuration.xml  
  
# Start then stop eXo Platform Tomcat  
RUN cd /tmp/ && \  
curl -L -o start_and_auto_shutdown_tomcat.sh
https://raw.githubusercontent.com/exo-docker/exo-maven/master/exo-maven-setup-
done/start_and_auto_shutdown_tomcat.sh && \  
chmod +x start_and_auto_shutdown_tomcat.sh &&
./start_and_auto_shutdown_tomcat.sh  

