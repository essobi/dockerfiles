FROM nimmis/java:openjdk-8-jdk  
  
MAINTAINER rehf27 <james@rehf27.com>  
  
#non-interactive installation  
ENV DEBIAN_FRONTEND noninteractive  
  
#default directory for SPIGOT-server  
ENV BUNGEECORD_HOME /bungeecord  
  
ADD bungeecord_init.sh /bungeecord_init.sh  
  
RUN chmod +x /bungeecord_init.sh  
  
# fast workaround  
RUN apt-get update && apt-get install -y wget git && apt-get clean all  
  
# Make special user for bungeecord to run in  
RUN useradd -s /bin/bash -d /bungeecord -m bungeecord  
  
# expose bungeecord port  
EXPOSE 25577  
#set default command  
CMD /bungeecord_init.sh  

