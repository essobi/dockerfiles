FROM frolvlad/alpine-oraclejdk8:slim  
VOLUME /tmp  
ADD ./target/document-service-0.0.1.jar document-service.jar  
RUN sh -c 'touch /document-service.jar'  
ENV JAVA_OPTS=""  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar /document-service.jar" ]

