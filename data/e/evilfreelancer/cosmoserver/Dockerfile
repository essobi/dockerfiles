FROM debian:stretch-slim  
  
ENV DOWNLOADS="https://cosmoteer.net/downloads"  
ENV VERSION="0.14.0"  
ENV FILE="Cosmoteer%20${VERSION}%20Setup.exe"  
ENV ROOT="/opt/cosmoteer"  
# Send proxy to container  
ARG PROXY  
ENV http_proxy=$PROXY  
  
# Add files to root folder  
ADD ["scripts", "/scripts"]  
  
# Install dependencied and cleanup after this  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install apt-transport-https gnupg dirmngr wget bash innoextract -y
--no-install-recommends \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian stretch main" >
/etc/apt/sources.list.d/mono-official-stable.list \  
&& apt-get update \  
&& apt-get install mono-complete -y --no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Run the builder scripts  
RUN /scripts/get_installer.sh \  
&& /scripts/extract_archive.sh \  
&& /scripts/cleanup.sh  
  
# Default port of server  
EXPOSE 35872:35872/udp  
  
# Run CosmoServer.exe withour arguments  
# https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-
entrypoint-interact  
ENTRYPOINT ["/usr/bin/mono", "/opt/cosmoteer/app/CosmoServer.exe"]  

