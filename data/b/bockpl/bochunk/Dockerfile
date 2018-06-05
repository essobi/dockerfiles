FROM ubuntu:16.04  
MAINTAINER Seweryn Sitarski  
  
# Instalacja klienta MFS  
# Nieinteraktywne apt  
#ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get -y install wget && \  
wget -O - http://ppa.moosefs.com/moosefs.key | apt-key add - && \  
echo "deb http://ppa.moosefs.com/moosefs-3/apt/ubuntu/xenial xenial main" >
/etc/apt/sources.list.d/moosefs.list && \  
apt-get update && \  
apt-get -y install moosefs-pro-chunkserver xfsprogs  
  
#RUN apt-get -y install lvm2 && sed -i 's/use_lvmetad = 1/use_lvmetad = 0/'
/etc/lvm/lvm.conf  
# Czyszczenie apt-a  
RUN apt-get -y purge wget && \  
apt-get -y autoremove && \  
apt-get -y clean  
  
ADD start.sh /  
  
EXPOSE 9422  
CMD ["/bin/bash","-c","/start.sh"]  

