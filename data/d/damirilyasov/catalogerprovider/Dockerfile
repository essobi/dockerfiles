FROM frolvlad/alpine-oraclejdk8:slim  
VOLUME /tmp  
ADD target/cataloger-provider-0.0.1-SNAPSHOT.jar app.jar  
ENV JAVA_OPTS=""  
EXPOSE 8080  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=/home/damir/projects/SemesterTaskfile:/dev/./uradondom
-jar /app.jar" ]

