FROM node:8.1.2  
RUN apt-get update  
RUN apt-get -y install sudo apt-utils  
RUN apt-get -y install git ssh tar zlib1g-dev gzip ca-certificates python
build-essential curl  
# Git LFS  
RUN curl -sSL https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | sudo -E bash -  
RUN apt-get -y install git-lfs  
# Setup git lfs  
RUN git lfs install  
  
CMD [ "bash" ]  

