FROM netflixoss/tomcat:7.0.64  
MAINTAINER Mayuresh Krishna <mayureshkrishna@gmail.com>  
  
RUN cd /tomcat/webapps &&\  
mkdir eureka &&\  
cd eureka &&\  
wget -q http://repo1.maven.org/maven2/com/netflix/eureka/eureka-
server/1.3.1/eureka-server-1.3.1.war &&\  
jar xf eureka-server-1.3.1.war &&\  
rm eureka-server-1.3.1.war &&\  
chgrp -R 0 /tomcat &&\  
chmod -R g+rwX /tomcat  
  
ADD config.properties /tomcat/webapps/eureka/WEB-INF/classes/config.properties  
ADD eureka-client-test.properties /tomcat/webapps/eureka/WEB-
INF/classes/eureka-client-test.properties  
ADD eureka-server-test.properties /tomcat/webapps/eureka/WEB-
INF/classes/eureka-server-test.properties  
  
EXPOSE 8080  
ENTRYPOINT ["/tomcat/bin/catalina.sh"]  
  
CMD ["run"]

