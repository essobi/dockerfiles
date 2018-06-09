FROM tomcat:8-jre8  
  
MAINTAINER Mitsumasa Sugimoto <sugimoto@mashbrains.jp>  
  
ENV CATALINA_OPTS="-Xmx2048m -server"  
RUN curl
"http://maven.forgerock.org/repo/releases/org/forgerock/openam/openam-
server/13.0.0/openam-server-13.0.0.war" -o openam.war && \  
mv openam.war $CATALINA_HOME/webapps/openam.war  
  
ADD run-openam.sh /tmp/run-openam.sh  
  
RUN chmod +x /tmp/run-openam.sh  
  
CMD ["/tmp/run-openam.sh"]

