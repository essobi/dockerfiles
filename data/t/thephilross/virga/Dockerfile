# VirGA Docker  
FROM ubuntu:14.04  
MAINTAINER Philipp Ross <philippross369@gmail.com>  
  
# Install basic dependencies  
RUN apt-get update && apt-get install -y \  
git-core \  
build-essential \  
wget && \  
apt-get clean  
  
RUN git clone https://bitbucket.org/szparalab/virga.git && \  
cd /virga && \  
bash VirGA_install.sh && \  
export PATH=/virga/Pipeline/:$PATH && \  
VirGA_Pipeline_Build.sh  
  

