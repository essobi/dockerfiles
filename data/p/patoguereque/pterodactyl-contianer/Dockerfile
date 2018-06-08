# ----------------------------------  
# Pterodactyl Core Dockerfile  
# Environment: Java  
# Minimum Panel Version: 0.6.0  
# ----------------------------------  
FROM openjdk:8-jre  
  
MAINTAINER MegaPlanet, <info@megaplanet.net>  
  
#RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
# && DEBIAN_FRONTEND=noninteractive apt-get -y install apt-utils \  
# && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade \  
# && DEBIAN_FRONTEND=noninteractive apt-get -y install curl ca-certificates
openssl git tar bash sqlite \  
# && DEBIAN_FRONTEND=noninteractive useradd -d /home/container container  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
imagemagick \  
lsof \  
nano \  
sudo \  
vim \  
jq \  
mysql-client \  
python \  
rsync \  
&& apt-get clean  
  
RUN DEBIAN_FRONTEND=noninteractive useradd -d /home/container container  
  
ADD
https://github.com/itzg/restify/releases/download/1.0.4/restify_linux_amd64
/usr/local/bin/restify  
ADD https://github.com/itzg/rcon-cli/releases/download/1.3/rcon-
cli_linux_amd64 /usr/local/bin/rcon-cli  
RUN chmod +x /usr/local/bin/*  
  
USER container  
ENV USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

