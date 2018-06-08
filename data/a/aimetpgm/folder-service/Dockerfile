FROM frolvlad/alpine-oraclejdk8:slim  
VOLUME /tmp  
ADD ./target/folder-service-0.0.1.jar folder-service.jar  
RUN sh -c 'touch /folder-service.jar'  
ENV JAVA_OPTS=""  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar /folder-service.jar" ]

