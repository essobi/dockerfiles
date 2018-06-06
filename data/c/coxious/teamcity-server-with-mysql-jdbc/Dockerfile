FROM jetbrains/teamcity-server:latest  
  
WORKDIR /root  
  
RUN apt-get update && apt-get install -y wget  
  
RUN wget http://central.maven.org/maven2/mysql/mysql-connector-
java/5.1.42/mysql-connector-java-5.1.42.jar -O /opt/teamcity/lib/mysql-
connector-java-5.1.42.jar  

