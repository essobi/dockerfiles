FROM maven:3-jdk-8  
WORKDIR /code  
COPY . /code/  
# set switch that enables correct JVM memory allocation in containers  
ENV JAVA_OPTS "-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap"  
ENV MAVEN_OPTS "-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap"  
RUN mvn compile  
  
ENTRYPOINT mvn -q exec:java -Dexec.args=/data

