FROM debian:stretch  
  
RUN apt-get -y update && apt-get -y upgrade && \  
apt-get -y install \  
strace \  
alsa-utils \  
build-essential \  
git \  
golang \  
wget \  
curl \  
libcap2-bin \  
nmap \  
lua5.2 \  
luajit \  
zsh \  
pdf2svg \  
ghostscript \  
imagemagick \  
net-tools \  
python3 \  
s3cmd \  
sox \  
webfs \  
vim  
  
RUN mkdir -p /go  
ENV GOPATH=/go  
  
CMD ["bash"]  

