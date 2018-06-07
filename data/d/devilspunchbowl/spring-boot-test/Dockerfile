FROM zenika/alpine-maven  
VOLUME /tmp  
COPY . .  
  
RUN mvn package  
RUN cp target/demo-spring-docker-simple-0.0.1-SNAPSHOT.jar ../app.jar  
RUN cd .. && ls  
ENV JAVA_OPTS=""  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar /app.jar" ]

