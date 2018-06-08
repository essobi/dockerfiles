FROM maven:3 AS builder  
WORKDIR /app  
COPY . /app  
RUN mvn install  
  
FROM fabric8/java-alpine-openjdk8-jre  
ENV AB_OFF=true \  
TZ=America/Sao_Paulo \  
JAVA_APP_NAME="demo" \  
JAVA_OPTIONS="-Xmx128m"  
COPY \--from=builder /app/target/*.jar /deployments

