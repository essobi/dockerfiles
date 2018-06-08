FROM java:8-jdk-alpine as Builder  
  
RUN apk update  
RUN apk add git  
  
ADD
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
/build/BuildTools.jar  
  
WORKDIR /build/  
  
RUN java -jar BuildTools.jar --rev latest  
  
FROM store/oracle/serverjre:8  
COPY \--from=0 /build/spigot*.jar /spigot/spigot.jar  
  
COPY eula.txt /spigot/eula.txt  
COPY server.properties /spigot/server.properties  
COPY spigot.yml /spigot/spigot.yml  
  
WORKDIR /spigot/  
  
EXPOSE 25565  
CMD java -jar spigot.jar  

