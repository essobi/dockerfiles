FROM java:8  
RUN apt-get update && apt-get install -y maven  
ADD . /usr/local/alphacore  
RUN update-java-alternatives --set java-1.8.0-openjdk-amd64 && cd
/usr/local/alphacore && mvn install && chmod -R 777
/usr/local/alphacore/target/  
EXPOSE 8088  
cmd ["java", "-jar", "/usr/local/alphacore/target/core-0.0.1-SNAPSHOT.jar"]

