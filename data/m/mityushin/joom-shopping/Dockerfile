# -- FIRST IMAGE WITH SRC --  
FROM jimador/docker-jdk-8-maven-node  
MAINTAINER Igor Konovalov "rogee.nok@gmail.com"  
COPY client ./home/joom/src/client  
COPY server ./home/joom/src/server  
COPY pom.xml ./home/joom/src/  
# MAKE BUILD SRC  
# --------------  
RUN mvn -f ./home/joom/src/pom.xml clean package  
  
# -- SECOND IMAGE WITH JAR ONLY  
FROM anapsix/alpine-java  
COPY \--from=0 /home/joom/src/server/target/server-0.1.jar /home/joom-app.jar  
ENTRYPOINT ["java","-jar","/home/joom-app.jar"]  
EXPOSE 8090

