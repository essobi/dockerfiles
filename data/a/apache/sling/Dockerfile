FROM openjdk:8-jre-alpine  
MAINTAINER dev@sling.apache.org  
  
# build on top of the released Launchpad  
RUN mkdir -p /opt/sling  
RUN wget
https://repo1.maven.org/maven2/org/apache/sling/org.apache.sling.starter/10/org.apache.sling.starter-10.jar
-O /opt/sling/org.apache.sling.starter.jar  
  
# sha1sum.txt must be updated when switching to a different jar,  
# or docker build will fail  
COPY sha1sum.txt /tmp  
RUN sha1sum -c /tmp/sha1sum.txt  
  
WORKDIR /opt/sling/  
EXPOSE 8080  
VOLUME /opt/sling/sling  
  
ENV JAVA_OPTS -Xmx512m  
ENV SLING_OPTS ''  
CMD exec java $JAVA_OPTS -jar org.apache.sling.starter.jar $SLING_OPTS  

