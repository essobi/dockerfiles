FROM debitux/x11-base:latest  
  
MAINTAINER sekhmet <sekhmet@debitux.com>  
  
RUN \  
apt-get update && \  
apt-get install -y cmake tmux htop gcc g++ libboost-all-dev qt5-default
postgresql-server-dev-all gdb valgrind && \  
  
apt-get -y -q autoclean && apt-get -y -q autoremove &&\  
apt-get -y clean && \  
  
rm -rf /var/lib/apt/lists/* \  
/usr/share/doc /usr/share/doc-base \  
/usr/share/man /usr/share/locale /usr/share/zoneinfo  
  
  
  
  

