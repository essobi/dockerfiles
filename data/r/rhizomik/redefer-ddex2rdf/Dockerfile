FROM anapsix/alpine-java  
VOLUME /tmp  
ADD target/ddex2rdf-0.2.0.jar app.jar  
RUN sh -c 'touch /app.jar'  
EXPOSE 8080  
ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar
/app.jar  

