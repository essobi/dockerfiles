FROM ubuntu:xenial  
  
RUN \  
apt-get update && \  
apt-get install -y \  
build-essential \  
libc6-dev-i386 \  
ncurses-dev \  
rsync \  
curl \  
git  
  
RUN \  
curl -LO $(echo \  
https://github.com$(curl -L https://github.com/peco/peco/releases/latest | \  
grep -oE "/peco/peco/releases/download/.+/.+amd64.tar.gz")) && \  
tar xvzf peco_linux_amd64.tar.gz && \  
mv peco_linux_amd64/peco /usr/local/bin && \  
rm -rf peco_linux_amd64*  
  
WORKDIR /work  

