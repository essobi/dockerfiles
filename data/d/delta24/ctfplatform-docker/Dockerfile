FROM ubuntu:12.04  
MAINTAINER delta24  
  
WORKDIR /root  
  
#RUN apt-get update && apt-get upgrade -y --force-yes  
#RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10  
#RUN echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen" | tee -a /etc/apt/sources.list.d/10gen.list  
# rest of the dependencies will be installed by scripts  
RUN apt-get -y update && apt-get -y install sudo git  
  
RUN git clone https://github.com/picoCTF/CTF-Platform.git  
  
RUN cd /root/CTF-Platform/  
  
RUN sh /root/CTF-Platform/scripts/install_deps.sh  
  

