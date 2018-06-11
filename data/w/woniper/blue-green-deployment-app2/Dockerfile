FROM java:8  
MAINTAINER woniper <leekw3747@gmail.com>  
  
VOLUME /tmp  
ADD app2.jar app2.jar  
EXPOSE 8889  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app2.jar"]

