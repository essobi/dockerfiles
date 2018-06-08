FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q && \  
apt-get dist-upgrade -o DPkg::options::='--force-confdef' -o Dpkg::Options::='
--force-confold' -y && \  
apt-get install build-essential apt-utils gzip gnupg \  
-o DPkg::options::='--force-confdef' -o Dpkg::Options::='--force-confold' -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ADD ./update-repo /usr/sbin/update-repo  

