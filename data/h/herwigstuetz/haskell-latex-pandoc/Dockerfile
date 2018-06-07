FROM herwigstuetz/latex-pandoc:latest  
MAINTAINER herwig@herwigstuetz.com  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential zlib1g-dev \  
git \  
unzip \  
libssl-dev \  
libfile-slurp-perl \  
libipc-run-perl \  
libicu-dev  
  
RUN wget -qO- https://get.haskellstack.org/ | sh  
  
RUN wget -O git-lfs_2.2.1_amd64.deb https://packagecloud.io/github/git-
lfs/packages/ubuntu/xenial/git-lfs_2.2.1_amd64.deb/download \  
&& dpkg --install git-lfs_2.2.1_amd64.deb \  
&& git lfs install  
  
WORKDIR /tmp  

