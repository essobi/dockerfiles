FROM ubuntu:16.04  
EXPOSE 25565  
HEALTHCHECK CMD (ss -plunt 2>/dev/null | grep 25565) || exit 1  
  
# The specific version of the Spigot server that you want to build  
# e.g. "1.12.2" or "latest"  
ENV REV latest  
  
ENV UID=1000  
ENV GID=1000  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
openjdk-8-jre \  
sudo  
  
RUN groupadd -g $GID minecraft && \  
useradd -s /bin/bash -d /minecraft -m minecraft -g minecraft && \  
usermod -aG sudo minecraft && \  
usermod --uid $UID minecraft && \  
groupmod --gid $GID minecraft  
  
RUN echo "minecraft ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
ADD ./minecraft/ /minecraft/  
  
RUN chmod +x /minecraft/start.sh  
  
USER minecraft  
  
VOLUME /minecraft/  
  
ENTRYPOINT ["/minecraft/start.sh"]  

