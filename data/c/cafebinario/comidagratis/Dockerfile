FROM expertsystems/oracle-jdk8:latest  
MAINTAINER Alexandre Moraes <alexandre.msl@gmail.com>  
VOLUME /tmp  
EXPOSE 10100:10100  
ADD cafebinario-register-0.0.1.jar app.jar  
RUN sh -c 'touch /app.jar'  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]

