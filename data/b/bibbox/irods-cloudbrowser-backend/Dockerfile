# iRODS Cloud Browser Backend  
#  
# VERSION 0.0.2  
#  
# 0.0.1 : not existing  
# 0.0.2 : splitting up the iRODS Cloud Browser frontend and backend  
FROM tomcat:7.0-jre7  
  
MAINTAINER Robert Reihs <robert.reihs@gmail.com>  
  
RUN apt-get update \  
&& apt-get -y update \  
&& wget https://github.com/DICE-UNC/irods-cloud-
browser/releases/download/1.0.1-RELEASE/irods-cloud-backend-config.groovy \  
&& wget https://github.com/DICE-UNC/irods-cloud-
browser/releases/download/1.0.1-RELEASE/irods-cloud-backend.war  
  
RUN rm -r $CATALINA_HOME/webapps/docs \  
&& rm -r $CATALINA_HOME/webapps/examples \  
&& mv irods-cloud-backend.war $CATALINA_HOME/webapps/irods-cloud-backend.war  
  
ADD scripts /scripts  
WORKDIR /scripts  
RUN chmod a+x *.sh  
  
ENTRYPOINT [ "/scripts/entrypoint.sh" ]

