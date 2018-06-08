FROM popkirby/openjdk-7-jdk  
MAINTAINER popkirby <popkirby@gmail.com>  
  
RUN mkdir /tmp/spigot  
RUN mkdir /tmp/spigot-tmp  
  
RUN mkdir /minecraft_data  
  
ADD ./scripts/spigot-update.sh /tmp/spigot-tmp/spigot-update.sh  
ADD ./scripts/spigot-update-init.sh /tmp/spigot-tmp/spigot-update-init.sh  
  
RUN chmod +x /tmp/spigot-tmp/spigot-update.sh  
RUN chmod +x /tmp/spigot-tmp/spigot-update-init.sh  
  
CMD '/tmp/spigot-tmp/spigot-update-init.sh'  
  

