FROM ubuntu:16.04  
#MAINTAINER Jaka Hudoklin <jaka@gatehub.net>  
MAINTAINER Cryptcoin Junkey <cryptcoin.junkey@gmail.com>  
  
# Official instructions from  
# https://ripple.com/build/rippled-setup/#installation-on-ubuntu-with-alien  
RUN apt-get update  
RUN apt-get install -y yum-utils alien  
RUN rpm -Uvh https://mirrors.ripple.com/ripple-repo-el7.rpm  
RUN yumdownloader --enablerepo=ripple-stable --releasever=el7 rippled  
RUN rpm --import https://mirrors.ripple.com/rpm/RPM-GPG-KEY-ripple-release &&
rpm -K rippled*.rpm  
RUN alien -i --scripts rippled*.rpm && rm rippled*.rpm  
  
# 31235 is for GKE's LoadBalancer.  
EXPOSE 31235 51235 5006  
ENTRYPOINT ["/opt/ripple/bin/rippled"]  

