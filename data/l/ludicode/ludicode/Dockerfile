from debian:stretch  
run apt-get update && \  
apt-get install -y maven openjdk-8-jdk && \  
apt-get clean  
add pom.xml /srv/ludicode/  
workdir /srv/ludicode/  
run mvn install  
add src /srv/ludicode/src/  
run mvn package  
expose 8080  
cmd ["java","-jar","target/dependency/jetty-runner.jar","target/Ludicode.war"]  

