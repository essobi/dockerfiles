## Image to build from sources  
FROM debian:latest  
MAINTAINER Sylvain Boily "sboily@proformatique.com"  
MAINTAINER XiVO dev team "dev+docker@proformatique.com"  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
# Add dependencies  
RUN apt-get -qq update && \  
apt-get -qq -y install \  
aptitude \  
build-essential \  
git \  
libasound2-dev \  
libncurses-dev \  
libpcap-dev \  
python-dev \  
python-setuptools \  
python-twisted \  
python-pip \  
python-yaml \  
sudo \  
wget  
  
# Install Asterisk  
WORKDIR /usr/src  
RUN git clone \--depth 1 https://gerrit.asterisk.org/asterisk && \  
cd /usr/src/asterisk/contrib/scripts && \  
./install_prereq install && \  
cd /usr/src/asterisk && \  
./configure --enable-dev-mode --with-pjproject-bundled && \  
make menuselect && \  
menuselect/menuselect --enable TEST_FRAMEWORK menuselect.makeopts && \  
make && \  
make install && \  
# make samples creates asterisk.conf, musiconhold.conf, etc.  
make samples && \  
cd /usr/src && \  
rm -rf asterisk  
  
# Install testsuite  
WORKDIR /usr/src  
RUN git clone \--depth 1 https://gerrit.asterisk.org/testsuite && \  
cd /usr/src/testsuite && \  
contrib/scripts/install_prereq install  
  
WORKDIR /usr/src/testsuite  
CMD ./runtests.py  

