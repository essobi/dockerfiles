FROM dockerfile/ubuntu  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
WORKDIR /data  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ENV PULSE_SERVER unix:/root/pulse/native  
VOLUME /root/pulse/  
  
RUN apt-get update && \  
apt-get install software-properties-common libxrender1 -y && \  
add-apt-repository ppa:minecraft-installer-peeps/minecraft-installer && \  
apt-get update && \  
apt-get install minecraft-installer -y  
  
CMD java -jar /usr/share/minecraft/minecraft.jar  
  
VOLUME /root/.minecraft/  
  
ENTRYPOINT java -jar /usr/share/minecraft/minecraft.jar  

