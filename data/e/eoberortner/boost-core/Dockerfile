FROM java:7  
# Install maven  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get install -y maven --fix-missing  
  
# the working directory  
WORKDIR /code  
  
ADD pom.xml /code/pom.xml  
RUN mvn dependency:resolve  
RUN mvn verify  
  
##--------------------------------------  
## Build boost-core.jar w/ dependencies  
##  
# Compile and package into an executable jar  
# including all dependencies  
RUN mvn assembly:assembly  
  
## execute the jar file  
RUN mv /code/target/boost-core-0.0.1-SNAPSHOT-jar-with-dependencies.jar boost-
core.jar  
ENTRYPOINT java -jar boost-core.jar  
##--------------------------------------  
###--------------------------------------  
### Build boost-core.jar w/o dependencies  
###  
#  
## Compile and package into an executable jar  
## including all dependencies  
#RUN mvn package  
#  
### execute the jar file  
#RUN mv /code/target/boost-core-0.0.1-SNAPSHOT.jar boost-core-02.jar  
#ENTRYPOINT java -jar boost-core-02.jar  
###--------------------------------------  

