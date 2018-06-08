FROM nimmis/java:openjdk-8-jdk  
  
MAINTAINER Giulio De Pasquale <me@krishath.it>  
  
#non-interactive installation  
ENV DEBIAN_FRONTEND noninteractive  
  
#default directory for SPIGOT-server  
ENV SPIGOT_HOME /home/minecraft  
  
ADD spigot_init.sh /spigot_init.sh  
  
RUN chmod +x /spigot_init.sh  
  
# fast workaround  
RUN apt-get update && apt-get install -y wget git && apt-get clean all  
  
# Make special user for minecraft to run in  
RUN useradd -s /bin/bash -m minecraft && \  
chown minecraft:minecraft $SPIGOT_HOME -R  
  
VOLUME $SPIGOT_HOME  
USER minecraft  
  
# expose minecraft port  
EXPOSE 25565  
  
#set default command  
CMD /spigot_init.sh  

