#
-----------------------------------------------------------------------------  
# docker-minecraft  
#  
# Builds a basic docker image that can run a Minecraft server  
# (http://minecraft.net/).  
#
-----------------------------------------------------------------------------  
# Base system is the LTS version of Ubuntu.  
FROM store/oracle/serverjre:8  
RUN yum -y install wget curl which  
  
# Load in all of our config files.  
ADD ./ftb /ftb  
  
# Fix all permissions  
RUN chmod -R 0777 /ftb  
  
RUN chmod +x /ftb/ServerStart.sh  
  
# 25565 is for minecraft  
EXPOSE 25565  
# /data contains static files and database  
VOLUME ["/ftb/mods", "/ftb/config", "/ftb/scripts", "/ftb/world"]  
  
WORKDIR /ftb  
  
ENV JAVA_HOME /usr/java/latest  
  
RUN ./FTBInstall.sh  
  
# /start runs it.  
CMD ["./ServerStart.sh"]  

