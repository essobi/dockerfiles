FROM ubuntu:16.04  
MAINTAINER km mukku <mukku.km@live.com>  
  
# Official instructions from  
# https://ripple.com/build/rippled-setup/#installation-on-ubuntu-with-alien  
COPY rippled.cfg /etc/opt/ripple/  
#COPY validators.txt /etc/  
RUN apt-get update  
RUN apt-get install -y yum-utils alien  
RUN rpm -Uvh https://mirrors.ripple.com/ripple-repo-el7.rpm  
RUN yumdownloader --enablerepo=ripple-stable --releasever=el7 rippled  
RUN rpm --import https://mirrors.ripple.com/rpm/RPM-GPG-KEY-ripple-release &&
rpm -K rippled*.rpm  
RUN alien -i --scripts rippled*.rpm && rm rippled*.rpm  
  
EXPOSE 5005  
EXPOSE 6006  
ENTRYPOINT ["/opt/ripple/bin/rippled"]  

