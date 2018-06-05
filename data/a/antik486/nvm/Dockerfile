FROM centos:centos7  
MAINTAINER antik486 <antik486@gmail.com>  
  
RUN yum -y update; \  
yum -y install git tar; \  
yum clean all  
  
RUN git clone https://github.com/creationix/nvm.git /DATA/nvm && \  
cd /DATA/nvm && \  
git checkout `git describe --abbrev=0 --tags`  
  
RUN /bin/bash -c "source /DATA/nvm/nvm.sh; nvm install v0.10.35; nvm alias
default v0.10.35; nvm use default v0.10.35"  
RUN /bin/bash -c "echo \"[[ -s /DATA/nvm/nvm.sh ]] && . /DATA/nvm/nvm.sh\" >>
/etc/profile.d/nvm.sh"  
  
VOLUME ["/DATA/app"]  
  
WORKDIR /DATA/app  
  
ENTRYPOINT ["bash"]  

