FROM docker.io/centos:centos7  
  
MAINTAINER Leo Gao <aoingl@gmail.com>  
  
# install basic utilities  
RUN yum update -y \  
&& yum install -y epel-release psmisc gcc gcc-c++ net-tools wget curl jq
python java-1.8.0-openjdk-devel maven git vim passwd less tree util-linux
binutils unzip tar xz-utils gzip git-svn python2-pip golang golang-src golang-
bin make sudo  
  
# install node js to latest stable: 8.9.4  
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -  
RUN yum -y install nodejs  
  
# create workspace directory to share to all  
RUN mkdir -p /workspace && chmod -R 777 /workspace  
  
# install ninja for useful functions  
RUN curl -s -L https://github.com/gaol/ninja/raw/master/install.sh | bash  
  

