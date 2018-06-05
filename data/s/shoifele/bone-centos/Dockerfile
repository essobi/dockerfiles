# shoifele/bone Centos7 Version  
FROM centos:7  
  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
  
ENV REFRESHED_AT="2016-04-16"  
ADD rootfs /  
  
RUN yum install epel-release -y \  
&& yum upgrade -y \  
&& yum install -y \  
git \  
less \  
vim \  
wget \  
net-tools \  
locales \  
sendmail \  
openssl \  
ca-certificates \  
bzip2 \  
&& yum clean all  
  
CMD ["/init"]  

