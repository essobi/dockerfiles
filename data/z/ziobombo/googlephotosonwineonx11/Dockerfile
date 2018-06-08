# DOCKER-VERSION 1.0  
FROM dit4c/dit4c-container-x11:debian  
LABEL maintainer="riccardo.casazza@gmail.com"  
  
RUN wget -q "http://deb.playonlinux.com/public.gpg" -O- | apt-key add -  
RUN wget http://deb.playonlinux.com/playonlinux_squeeze.list -O
/etc/apt/sources.list.d/playonlinux.list  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install
--install-recommends -y \  
playonlinux  

