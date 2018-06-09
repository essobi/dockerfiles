FROM alpine:3.3  
MAINTAINER Stein Fletcher <steinfletcher@gmail.com>  
  
WORKDIR /app  
  
RUN apk --update add openjdk8-jre  
  
RUN wget https://repo1.maven.org/maven2/com/netflix/hystrix/hystrix-
dashboard/1.5.1/hystrix-dashboard-1.5.1.war -O hystrix-dashboard.war  
  
RUN wget https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
runner/9.3.7.v20160115/jetty-runner-9.3.7.v20160115.jar -O jetty-runner.jar  
  
EXPOSE 8080  
CMD [ "java", "-jar", "jetty-runner.jar", "hystrix-dashboard.war" ]  
  

