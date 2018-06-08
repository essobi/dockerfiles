# ----------------------------------  
# Pterodactyl Core Dockerfile  
# Environment: Java  
# Minimum Panel Version: 0.6.0  
# ----------------------------------  
FROM openjdk:8-jre  
  
MAINTAINER MegaPlanet, <info@megaplanet.net>  
  
RUN apt-get update && \  
apt-get install -y \  
imagemagick \  
lsof \  
nano \  
sudo \  
vim \  
jq \  
mysql-client \  
python \  
rsync \  
curl \  
&& apt-get clean  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
#RUN useradd -d /home/container container  
ADD
https://github.com/itzg/restify/releases/download/1.0.4/restify_linux_amd64
/usr/local/bin/restify  
ADD https://github.com/itzg/rcon-cli/releases/download/1.3/rcon-
cli_linux_amd64 /usr/local/bin/rcon-cli  
RUN chmod +x /usr/local/bin/*  
  
#USER container  
#ENV USER container  
ENV HOME /home/container  
#RUN usermod -aG docker container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

