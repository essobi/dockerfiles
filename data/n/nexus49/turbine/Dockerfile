FROM asna/java8:wheezy  
  
WORKDIR /opt/turbine  
  
EXPOSE 8080  
RUN apt-get update && apt-get install curl unzip -y && \  
curl https://repo1.maven.org/maven2/com/netflix/turbine/turbine-
web/1.0.0/turbine-web-1.0.0.war -o turbine-web-1.0.0.war && \  
curl https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
runner/9.2.7.v20150116/jetty-runner-9.2.7.v20150116.jar -o jetty-runner.jar &&
\  
unzip -d app/ turbine-web-1.0.0.war && \  
rm turbine-web-1.0.0.war  
  
CMD [ "java", "-jar", "jetty-runner.jar", "app" ]  
  
ONBUILD COPY resources/config.properties /opt/turbine/app/WEB-
INF/classes/config.properties  

