FROM mono:latest  
  
MAINTAINER Jan Suchotzki <jan@inginform.de>  
  
# Git installieren  
RUN apt-get update -y \  
&& apt-get install -y git \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# HalloDocker Quellcode holen  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
RUN git clone https://github.com/inginform/hallo-docker-mit-Mono.git .  
  
# Quellcode kompilieren  
WORKDIR /usr/src/app/Code  
RUN mcs HalloDocker.cs  
  
# Ausführen  
CMD ["mono", "HalloDocker.exe"]

