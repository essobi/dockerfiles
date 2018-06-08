FROM java:8  
VOLUME /tmp  
ADD https://dl.bintray.com/vincent/artifact-sandbox/simpleservice-latest.jar
app.jar  
RUN sh -c 'touch /app.jar'  
EXPOSE 8080  
ENV JAVA_OPTS=""  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar /app.jar" ]

