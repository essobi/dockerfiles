FROM tomcat:7-jre8  
MAINTAINER Paul Velez "paul@relayrides.com"  
ENV MYSQL_ROOT_PASSWORD relayrides  
ENV LC_ALL en_US  
ENV CATALINA_OPTS -javaagent:$CATALINA_HOME/jetty-alpn-agent-2.0.3.jar  
  
RUN sed -i 's/INFO/DEBUG/g' /usr/local/tomcat/conf/logging.properties  
RUN wget -O jetty-alpn-agent-2.0.3.jar
"http://search.maven.org/remotecontent?filepath=org/mortbay/jetty/alpn/jetty-
alpn-agent/2.0.3/jetty-alpn-agent-2.0.3.jar"  
  
VOLUME ["/data", "/usr/local/tomcat/webapps", "/usr/share/GeoIP"]  

