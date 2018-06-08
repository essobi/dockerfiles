FROM openjdk:8u131-jdk-alpine as build  
WORKDIR /app  
COPY . .  
RUN ./gradlew shadowJar  
  
FROM openjdk:8u131-jre-alpine  
WORKDIR /app  
COPY \--from=build /app/build/libs/kubectl-login.jar .  
ENTRYPOINT ["java", \  
"-XX:+UnlockExperimentalVMOptions", \  
"-XX:+UseCGroupMemoryLimitForHeap", \  
"-XX:MaxRAMFraction=1", \  
"-XshowSettings:vm", \  
"-XX:+PrintGCDetails", \  
"-XX:+PrintGCTimeStamps", \  
"-XX:+PrintGCDateStamps", \  
"-jar", "kubectl-login.jar"]

