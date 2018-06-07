# Reference from Spring Boot with Docker - https://spring.io/guides/gs/spring-
boot-docker/  
FROM frolvlad/alpine-oraclejdk8:slim  
  
# fix wget issue with SSL: https://github.com/Yelp/dumb-init/issues/73  
RUN apk update && apk add ca-certificates wget && update-ca-certificates &&
apk add openssl  
  
VOLUME /tmp  
VOLUME /tmp/keystores  
RUN wget https://github.com/tingjan1982/password-
keeper/releases/download/master-snapshot/passkeeper-0.0.1-SNAPSHOT.jar -O
passkeeper.jar  
RUN sh -c 'touch /passkeeper.jar'  
ENV JAVA_OPTS="-Dsecurity.keystore.location=/tmp/keystores"  
# Explains the java.security.egd property:
https://wiki.apache.org/tomcat/HowTo/FasterStartUp#Entropy_Source  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar /passkeeper.jar" ]  

