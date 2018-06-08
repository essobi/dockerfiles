# http://docs.docker.io/en/latest/use/builder/#from  
# use "docker images" to find <image>:<tag> pairs  
FROM ubuntu:12.04  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install --yes --no-install-recommends\  
wget\  
sudo\  
python-software-properties\  
pciutils # for grains  
RUN add-apt-repository --yes ppa:saltstack/salt  
RUN apt-get update  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -s /bin/true /sbin/initctl  
  
RUN apt-get install --yes --no-install-recommends\  
salt-minion  
  

