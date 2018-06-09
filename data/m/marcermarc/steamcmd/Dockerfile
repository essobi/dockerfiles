FROM debian:stretch-slim  
  
LABEL maintainer "docker@marcermarc.de"  
  
# -----------------------------------------------------  
# add "steam" user and group  
# install needed packages and curl to download steamcmd  
# downlaod and extract steamcmd and login first time  
# remove curl because it is not needed anymore  
# -----------------------------------------------------  
RUN addgroup steam \  
&& adduser --home /steam --disabled-password --ingroup steam steam \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get -y install lib32gcc1 curl \  
&& su -l steam -c " \  
mkdir cmd \  
&& curl -sqL
"https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar
-C cmd -zxf - \  
&& cmd/steamcmd.sh +login anonymous +quit \  
" \  
&& apt-get -y remove curl \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& apt-get -y purge  
  
WORKDIR /steam/cmd  
ENTRYPOINT "./steamcmd.sh"

