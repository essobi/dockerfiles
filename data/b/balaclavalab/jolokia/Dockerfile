FROM jetty:9.4.9-alpine  
  
ENV JOLOKIA_VERSION=1.5.0 JOLOKIA_JSR160_PROXY_ENABLED=TRUE  
  
RUN wget http://search.maven.org/remotecontent?filepath=org/jolokia/jolokia-
war/${JOLOKIA_VERSION}/jolokia-war-${JOLOKIA_VERSION}.war -O
/var/lib/jetty/webapps/jolokia.war  
  
EXPOSE 8080/tcp  
  
CMD ["java","-jar","/usr/local/jetty/start.jar"]  
  

