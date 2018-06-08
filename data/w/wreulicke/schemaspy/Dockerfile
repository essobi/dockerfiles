FROM openjdk:8-jdk-alpine  
  
ENV DRIVER_URL http://central.maven.org/maven2/mysql/mysql-connector-
java/5.1.39/mysql-connector-java-5.1.39.jar  
ENV APP_URL
https://github.com/schemaspy/schemaspy/releases/download/v6.0.0-rc2/schemaspy-6.0.0-rc2.jar  
  
WORKDIR /app  
  
RUN apk --no-cache add graphviz font-noto && \  
apk --no-cache add --virtual .builddep tzdata wget libressl && \  
wget -O mysql-connector-java.jar ${DRIVER_URL} && \  
wget -O schemaspy.jar ${APP_URL} && \  
apk del .builddep  

