############################################################  
# Dockerfile to run ET: Legacy containers  
# Based on Debian image  
############################################################  
# Set the base image to use to Ubuntu  
FROM debian:latest  
  
# Set the file maintainer (your name - the file's author)  
MAINTAINER Riccardo Casazza  
  
# Install prereqs  
RUN apt-get update && apt-get install -y \  
p7zip-full \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Wolfenstein: Enemy Territory Legacy  
RUN curl https://www.etlegacy.com/download/file/87 | tar xvz; mv
etlegacy-v2.75-x86_64 etlegacy  
RUN curl -o temp.exe
http://trackbase.eu/files//et/full/WolfET_2_60b_custom.exe; 7z e temp.exe
-oetlegacy/etmain etmain/pak*.pk3; rm temp.exe  
RUN echo "set sv_allowDownload \"1\"" >> etlegacy/etmain/etl_server.cfg  
RUN echo "set rconpassword \"etlegacy\"" >> etlegacy/etmain/etl_server.cfg  
RUN echo "set g_friendlyFire \"0\"" >> etlegacy/etmain/etl_server.cfg  
RUN sed -i "s|exec mapvotecycle.cfg|//exec mapvotecycle.cfg|g"
etlegacy/etmain/etl_server.cfg  
RUN sed -i "s|//exec campaigncycle.cfg|exec campaigncycle.cfg|g"
etlegacy/etmain/etl_server.cfg  
  
# Port to expose  
EXPOSE 27960/udp  
  
# Set the user to run etlegacy as daemon  
USER root  
  
# Set the entrypoint to etlegacy script  
WORKDIR /etlegacy  
ENTRYPOINT ./etlded_bot.sh  

