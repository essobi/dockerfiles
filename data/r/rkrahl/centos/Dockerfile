FROM centos:7  
MAINTAINER Rolf Krahl <rolf.krahl@helmholtz-berlin.de>  
  
# - Add home:Rotkraut:Docker and EPEL repositories,  
# - update,  
# - install tiny-init and a few other packages.  
RUN curl --silent --show-error --location \  
\--output /etc/yum.repos.d/Rotkraut.repo \  
http://download.opensuse.org/repositories/home:Rotkraut:Docker/CentOS_7/home:Rotkraut:Docker.repo
&& \  
yum -y install epel-release && \  
yum -y update && \  
yum --setopt='minrate=100' -y install \  
tiny-init \  
net-tools \  
openssl \  
pwgen  
  
ENTRYPOINT ["/usr/sbin/tiny-init"]  

