# ----------------------------------  
# Pterodactyl Core Dockerfile  
# Environment: Java (glibc support)  
# Minimum Panel Version: 0.6.0  
# ----------------------------------  
FROM ubuntu:latest  
  
MAINTAINER nobody, <support@pterodactyl.io>  
  
RUN \  
apt-get update \  
&& adduser container --home /home/container --gecos "" \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/ubuntu stable-xenial main"
| tee -a /etc/apt/sources.list \  
&& apt-get update \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -yq apt-utils \  
&& apt-get upgrade -yq \  
&& apt install -yq tzdata && dpkg-reconfigure tzdata \  
&& apt-get install -yq curl ca-certificates openssl git tar bash \  
&& apt install -yq mono-complete  
  
USER container  
ENV USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]

