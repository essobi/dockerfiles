############################################################  
# Dockerfile to build a server to run minecraft  
# Based on dockerfile / java  
############################################################  
  
FROM mhutter/java  
  
MAINTAINER Fabrizio Lungo <fab@lungo.co.uk>  
  
# Add Minecraft User  
RUN useradd -m mc -u 1000  
  
# Expose minecraft port  
EXPOSE 25565  
  
# Setup server directory  
RUN mkdir /srv/minecraft/  
RUN chown mc:mc /srv/minecraft/  
WORKDIR /srv/minecraft/  
  
# Add files  
ADD usr/local/share/minecraft/ /usr/local/share/minecraft/  
RUN ln -s /usr/local/share/minecraft/entrypoint /usr/local/bin/entrypoint  
  
# Run the server as the minecraft user  
USER 1000  
ENTRYPOINT entrypoint  

