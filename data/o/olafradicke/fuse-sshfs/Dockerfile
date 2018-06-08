#FROM fedora  
#FROM centos  
FROM debian:testing  
  
ENV sshuser "yourSshUser"  
ENV sshserver "yourSshServerName"  
ENV sshexport "yourSshExportDirectory"  
# Directory with ssh auth key  
VOLUME ["/roo/.ssh"]  
# Data volume  
VOLUME ["/data/sshfs"]  
  
COPY ./start.sh start.sh  
  
#RUN yum -y install fuse-sshfs  
RUN apt-get update && apt-get -y upgrade && apt-get -y install sshfs  
  
CMD ["/bin/bash", "start.sh"]  

