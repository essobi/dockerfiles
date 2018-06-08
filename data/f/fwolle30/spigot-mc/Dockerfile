FROM debian:latest  
  
MAINTAINER Frank Wolbring <fwolbring@googlemail.com>  
  
EXPOSE 25565 8123  
ADD init.sh /  
ADD
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
/  
  
RUN ["/bin/bash", "init.sh"]  
RUN java -jar /BuildTools.jar  
  
VOLUME /data  
WORKDIR /data  
  
CMD echo "eula=true" >> eula.txt && java -Xmx1G -jar /spigot-1.11.2.jar  

