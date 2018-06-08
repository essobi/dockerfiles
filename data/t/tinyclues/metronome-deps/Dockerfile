FROM quay.io/tinyclues/scala-deps:master  
  
RUN DISTRO="$(lsb_release -is | tr '[:upper:]' '[:lower:]')" && \  
CODENAME="$(lsb_release -cs)" && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF && \  
echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" >
/etc/apt/sources.list.d/mesosphere.list &&\  
apt-get -y update && \  
apt-get install -y mesos && \  
rm -rf /var/lib/apt/lists/*  

