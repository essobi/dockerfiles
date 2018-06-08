FROM nimmis/java-centos  
  
MAINTAINER SomosPNT "contacto@somospnt.com"  
# Path for logs  
RUN mkdir -p /tmp/spring-flow/logs  
  
VOLUME /tmp/spring-flow/logs  
  
# Port range for streams  
EXPOSE 7000-7010  
# Download spring cloud data flow server  
RUN wget -O app.jar
http://repo.spring.io/release/org/springframework/cloud/spring-cloud-dataflow-
server-local/1.2.3.RELEASE/spring-cloud-dataflow-server-
local-1.2.3.RELEASE.jar  
  
# Set tmp dir for logs  
ENV JAVA_OPTS="-Djava.io.tmpdir=/tmp/spring-flow/logs"  
# Run application  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar ./app.jar" ]

