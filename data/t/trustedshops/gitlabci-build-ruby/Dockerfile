FROM trustedshops/gitlabci-build-base:centos7  
  
RUN yum install -y which && \  
gpg \--keyserver hkp://keys.gnupg.net \--recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \  
curl -sSL https://get.rvm.io | /bin/bash -s stable \--with-default-
gems="bundler" && \  
. /etc/profile  

