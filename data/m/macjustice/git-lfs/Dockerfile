FROM ubuntu:xenial  
LABEL maintainer "macj@synapse.com"  
  
RUN apt-get update && apt-get -y install wget git -y && \  
wget https://packagecloud.io/github/git-lfs/packages/ubuntu/xenial/git-
lfs_2.1.1_amd64.deb/download -O git-lfs_2.1.1_amd64.deb && \  
dpkg -i git-lfs_2.1.1_amd64.deb  

