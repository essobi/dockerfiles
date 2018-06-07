#Use the last LTS version of ubuntu  
FROM ubuntu:16.04  
  
MAINTAINER kamaradeivanov  
  
######################## install prerequisite for steamcmd
###########################  
# Stop apt-get asking to get Dialog frontend  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install dependencies and clean  
RUN apt-get update && apt-get install -y \  
lib32gcc1 \  
curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
#### ######################################################################
####  
  
  
########################## install and run steam cmd
###########################  
# Add the steam user  
RUN adduser \  
\--disabled-login \  
\--shell /bin/bash \  
steam  
  
#Switch to the user steam  
USER steam  
  
# Download and extract steamcmd  
RUN mkdir /home/steam/steamcmd &&\  
cd /home/steam/steamcmd &&\  
curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz  
  
# Always run steam cmd on anonymous, download the app  
RUN chmod u+x /home/steam/steamcmd/steamcmd.sh  
RUN /home/steam/steamcmd/steamcmd.sh +login anonymous +quit  
#### ######################################################################
####  

