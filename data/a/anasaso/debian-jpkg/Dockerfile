FROM debian:jessie  
  
MAINTAINER Anas ASO <aso.anas@protonmail.com>  
  
RUN \  
bash -c 'echo -e "deb http://httpredir.debian.org/debian jessie main
contrib\ndeb http://httpredir.debian.org/debian jessie-updates main\ndeb
http://security.debian.org jessie/updates main" > /etc/apt/sources.list' && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install wget curl java-package libgl1-mesa-glx libgtk2.0-0 libxslt1.1
libxtst6 libxxf86vm1 -y --fix-missing && \  
useradd -ms /bin/bash java-packager  
  
USER java-packager  
  
WORKDIR /workdir  
  
VOLUME ["/workdir"]  
  
CMD ["--help"]  
  
ENTRYPOINT ["make-jpkg"]  

