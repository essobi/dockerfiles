FROM tomcat:7  
MAINTAINER Oliver Lade <oliver.lade@unimelb.edu.au>  
# See https://github.com/opensourceBIM/BIMserver/wiki/Install-on-Ubuntu  
ENV TOMCAT_HOME /usr/local/tomcat  
ENV BIMSERVER_APP $TOMCAT_HOME/webapps/bimserver  
  
# Delete the example Tomcat app to speed up deployment.  
RUN rm -rf $TOMCAT_HOME/webapps/examples  
  
ADD
https://github.com/opensourceBIM/BIMserver/releases/download/1.3.0-FINAL-2014-04-25/bimserver-1.3.0-FINAL-2014-04-25.war
$BIMSERVER_APP.war  
RUN unzip $BIMSERVER_APP.war -d $BIMSERVER_APP && rm $BIMSERVER_APP.war  

