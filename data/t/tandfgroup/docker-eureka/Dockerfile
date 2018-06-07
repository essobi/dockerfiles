FROM netflixoss/eureka:1.3.1  
ADD config/config.properties /tomcat/webapps/eureka/WEB-
INF/classes/config.properties  
ADD config/eureka-client-dev.properties /tomcat/webapps/eureka/WEB-
INF/classes/eureka-client-dev.properties  
ADD config/eureka-client-dev.properties /tomcat/webapps/eureka/WEB-
INF/classes/eureka-client.properties  
ADD config/eureka-server.properties /tomcat/webapps/eureka/WEB-
INF/classes/eureka-server.properties  
  
COPY scripts/* scripts/  
  
RUN chmod 777 -R scripts/  
  
ENTRYPOINT ["/scripts/start.sh"]

