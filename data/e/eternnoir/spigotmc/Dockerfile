#  
# A minecraft spigot server.  
#  
# Pull base image.  
FROM eternnoir/ubuntu-java:oracle-java7  
MAINTAINER Frank Wang "eternnoir@gmail.com"  
RUN apt-get -y update && apt-get install -y wget git  
  
RUN mkdir -p /tmp/sp  
RUN mkdir /basicdata  
WORKDIR /tmp/sp  
RUN wget -O BuildTools.jar
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar  
RUN java -jar BuildTools.jar  
RUN cp spigot-1.8.jar /basicdata  
ADD eula.txt /basicdata/eula.txt  
ADD server.properties /basicdata/server.properties  
ADD run.sh /  
  
WORKDIR /mcdata  
EXPOSE 25565  
ENV JVM_OPTS -Xmx1024M -Xms1024M  
VOLUME [ "/mcdata" ]  
CMD ["sh","/run.sh"]  
  

