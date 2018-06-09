FROM debian:stretch  
  
LABEL software="TelSeq"  
LABEL software.version="latest"  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Configure local  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
tar lzma libreadline7 gzip bzip2 gnupg2 unzip \  
openssh-client wget curl ca-certificates rsync \  
libglib2.0-0 libxext6 libsm6 libxrender1 git vim-nox make \  
htop parallel git-core build-essential zlib1g-dev \  
libncurses-dev cmake patch libnss-sss && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Software: Telseq  
RUN git clone https://github.com/zd1/telseq.git && \  
cp telseq/bin/ubuntu/telseq /usr/local/bin/ && \  
rm -rf $HOME/telse*  

