FROM dakue/tomcat-agent-bond:8-jre8  
MAINTAINER Daniel Kühne <dkhmailto@googlemail.com>  
  
RUN set -x && \  
rm -rf /usr/local/tomcat/webapps/ROOT && \  
curl -sSL "http://downloads.sourceforge.net/project/plantuml/plantuml.war" >
/usr/local/tomcat/webapps/ROOT.war  

