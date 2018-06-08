FROM openjdk:8-jdk  
  
MAINTAINER Long Vu "long@tlvu.ca"  
RUN useradd user --create-home && \  
apt-get update && apt-get install -y graphviz  
  
USER user  
# newer schemaspy: http://sourceforge.net/projects/schemaspy/files/schemaspy/  
# newer mysql connector: http://dev.mysql.com/downloads/connector/j/  
RUN mkdir $HOME/pkg && \  
curl --silent --location
https://github.com/schemaspy/schemaspy/releases/download/v6.0.0-rc2/schemaspy-6.0.0-rc2.jar
> $HOME/pkg/schemaSpy.jar && \  
curl --silent --location https://cdn.mysql.com/Downloads/Connector-J/mysql-
connector-java-5.1.44.tar.gz | tar -C $HOME/pkg/ -xzf - && \  
ln -s mysql-connector-java-5.1.44/mysql-connector-java-5.1.44-bin.jar
$HOME/pkg/mysql-conn.jar && \  
mkdir $HOME/workdir  
  
WORKDIR /home/user/workdir  
  
ENTRYPOINT ["java", "-jar", "/home/user/pkg/schemaSpy.jar"]  

