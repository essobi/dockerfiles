FROM openjdk:8-jdk-alpine  
ENV APP_URL=""  
ENV JAVA_OPTS=""  
ENV APP_OPTS=""  
VOLUME /tmp  
VOLUME /app  
COPY run.sh /app/  
RUN apk --no-cache --update add wget ca-certificates fontconfig ttf-dejavu  
ENTRYPOINT ["/app/run.sh"]  

