FROM centos:7  
  
MAINTAINER amazee.io hello@amazee.io  
  
RUN \  
curl https://dl.yarnpkg.com/rpm/yarn.repo --silent -o
/etc/yum.repos.d/yarn.repo && \  
curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - && \  
yum install -y \  
ocaml \  
elfutils-libelf-devel \  
nodejs \  
yarn \  
&& \  
yum clean all -y  

