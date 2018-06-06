FROM openjdk:8-jre-alpine  
RUN apk add --update tzdata && rm -rf /var/cache/apk/*  
ADD build/libs/fint-pwfa-consumer-*.jar /data/app.jar  
CMD ["java", "-jar", "/data/app.jar"]

