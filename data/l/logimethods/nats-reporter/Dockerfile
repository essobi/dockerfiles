FROM tomcat:8.5-alpine  
  
RUN apk --update add openjdk8  
  
COPY tomcat/WebContent/ webapps/nats-reporter/  
  
RUN cd webapps/nats-reporter/WEB-INF/src \  
&& mkdir ../classes \  
&& find -name "*.java" > sources.txt \  
&& javac -cp ../lib/*: -d ../classes @sources.txt \  
&& cd ../../../.. \  
&& apk del openjdk8  

