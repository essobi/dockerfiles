# Dockerfile  
FROM maven:3.5-jdk-8-alpine as BUILD  
COPY . /data/src/  
RUN mvn -f /data/src/pom.xml clean package -DskipTests  
  
FROM openjdk:8-jre  
ENV PORT=8080  
ENV TZ=Asia/Seoul  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
EXPOSE ${PORT}  
COPY \--from=BUILD /data/src/target/*.jar /data/ROOT.jar  
WORKDIR data  
CMD ["java", "-jar", "ROOT.jar"]  

