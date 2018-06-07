FROM openjdk:8-jdk-alpine  
VOLUME /tmp  
ADD build/libs/ledger-posting-rule.jar app.jar  
#ADD target/ledger-posting-rule.jar app.jar  
ENV JAVA_OPTS=""  
EXPOSE 8080  
ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar
/app.jar

