FROM ubuntu:16.04  
MAINTAINER R. Lejolivet <raphael.lejolivet@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get -y install letsencrypt &&
apt-get clean  
  
ADD run.sh /bin/run.sh  
ENTRYPOINT [ "/bin/run.sh" ]  
  
VOLUME /etc/letsencrypt  

