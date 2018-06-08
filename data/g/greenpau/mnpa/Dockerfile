FROM ubuntu:latest  
MAINTAINER Paul Greenberg @greenpau  
RUN apt-key adv --recv-keys \--keyserver keyserver.ubuntu.com 3B4FE6ACC0B21F32
&& \  
apt-get install -y software-properties-common && \  
apt-add-repository -y "deb http://archive.ubuntu.com/ubuntu/ trusty main
restricted universe multiverse" && \  
apt-add-repository -y ppa:ubuntu-toolchain-r/test && \  
apt-get update -qq && \  
apt-get install -qq gcc-5 g++-5 make git vim && \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 500  
RUN cd /tmp && cd mnpa || git clone https://github.com/greenpau/mnpa.git && cd
mnpa && make && make install  

