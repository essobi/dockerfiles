FROM frolvlad/alpine-oraclejdk8:slim  
VOLUME /tmp  
ADD ./target/approver-list-service-0.0.1.jar approver-list-service.jar  
RUN sh -c 'touch /approver-list-service.jar'  
ENV JAVA_OPTS=""  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar /approver-list-service.jar" ]

