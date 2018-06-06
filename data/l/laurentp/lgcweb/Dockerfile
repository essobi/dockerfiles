from debian  
run apt-get update && \  
apt-get install -y maven openjdk-7-jdk && \  
apt-get clean  
add pom.xml /srv/lgcWeb/  
workdir /srv/lgcWeb/  
run mvn install  
add src /srv/lgcWeb/src/  
volume ["/root"]  
expose 8080  
cmd mvn jetty:run  

