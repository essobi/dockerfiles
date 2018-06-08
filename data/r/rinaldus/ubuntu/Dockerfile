FROM ubuntu:latest  
ENV DEBIAN_FRONTEND noninteractive  
  
# Enable multiverse  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
  
# Upgrade distribution  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
  
# Russian localization  
RUN apt-get install -y locales && rm -rf /var/lib/apt/lists/* && localedef -i
ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias ru_RU.UTF-8  
ENV LANG ru_RU.utf8  
  
# Install necessary soft  
RUN apt-get update && apt-get install -y vim unzip unrar-free xz-utils  
  
# Set workdir  
WORKDIR /root  
VOLUME ["/root"]  
  

