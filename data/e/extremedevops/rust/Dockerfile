FROM debian:jessie  
MAINTAINER Leandro David Cacciagioni - <leandro.21.2008@gmail.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get dist-upgrade -qqy && \  
apt-get install -qqy --no-install-recommends wget && \  
mkdir /rust && \  
wget --no-check-certificate https://static.rust-
lang.org/dist/rust-1.2.0-x86_64-unknown-linux-gnu.tar.gz -O
/rust/rust-1.2.0-x86_64-unknown-linux-gnu.tar.gz && \  
cd /rust && \  
tar xzfv ./rust-1.2.0-x86_64-unknown-linux-gnu.tar.gz && \  
cd rust-1.2.0-x86_64-unknown-linux-gnu && \  
./install.sh && \  
cd / rm -rf /rust && \  
apt-get autoremove -qqy && \  
apt-get clean && apt-get autoclean && \  
rm -rf /usr/share/man/?? && rm -rf /usr/share/man/??_*  

