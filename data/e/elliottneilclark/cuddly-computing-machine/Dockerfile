FROM ubuntu  
MAINTAINER eclark@apache.org  
RUN apt-get -qq update && \  
apt-get install -y gdb gdbserver build-essential valgrind vim git && \  
apt-get -qq clean && \  
apt-get -y -qq autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ && \  
mkdir -p /var/lib/{apt,dpkg,cache,log}/ && \  
rm -rf /tmp/*  
  
RUN mkdir -p /usr/local/src/ && cd /usr/local/src/ && \  
git clone https://github.com/radare/radare2.git && \  
cd radare2 && \  
./sys/install.sh && \  
make symstall  
  
EXPOSE 80  

