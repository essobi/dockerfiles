FROM consol/ubuntu-xfce-vnc  
  
## Install a gedit  
USER 0  
RUN apt-get update \  
&& wget
https://github.com/Tribler/tribler/releases/download/v7.0.2/tribler_7.0.2_all.deb
\  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y ./tribler_7.0.2_all.deb  
  
## switch back to default user  
USER 1984  

