FROM galeone/archlinux-updated-aur  
MAINTAINER Paolo Galeone <nessuno@nerdz.eu>  
  
RUN pacaur -Syu ca-certificates openssl git nodejs npm gcc-libs --noconfirm  
  
USER root  
RUN useradd -m -s /bin/bash camo  
  
EXPOSE 8081  
VOLUME /home/camo  
COPY startup.sh /opt/  
  
USER camo  
ENTRYPOINT bash /opt/startup.sh  

