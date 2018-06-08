FROM ubuntu:17.04  
RUN apt-get update && apt-get install -y \  
autoconf \  
build-essential \  
clang \  
expect \  
git \  
hdf5-tools \  
iputils-ping \  
net-tools \  
libcurl4-gnutls-dev \  
libevent-dev \  
libgtk2.0-dev \  
libhdf5-dev \  
libhwloc-dev \  
liblua5.2-dev \  
libmunge-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpam0g-dev \  
librrd-dev \  
libssh2-1-dev \  
libssl-dev \  
man2html \  
munge \  
mysql-client \  
openssh-server \  
python \  
vim  
RUN echo "thisismysecretmungekeythatis32bytes" > /etc/munge/munge.key  
WORKDIR /slurm  
CMD ["/bin/bash"]  

