FROM debian:latest  
MAINTAINER Marcel Grossmann <whatever4711@gmail.com>  
  
WORKDIR /usr/local/bin  
  
RUN apt-get update  
RUN apt-get -y install wget build-essential fakeroot  
RUN apt-get -y install git  
RUN apt-get -y install debhelper autoconf automake libssl-dev graphviz python-
all python-qt4 python-zopeinterface python-twisted-conch libtool  
  
ADD build.sh /usr/local/bin/build.sh  
RUN chmod 755 /usr/local/bin/build.sh  
RUN bash -C "/usr/local/bin/build.sh"  
  
RUN apt-get -y install dkms module-assistant ipsec-tools python-twisted-web
init-system-helpers  
RUN apt-get -y install debconf-utils  
ADD racoon.debconf /usr/local/bin/racoon.debconf  
RUN cat racoon.debconf | debconf-set-selections  
RUN apt-get -y install racoon  
  
#RUN git clone https://github.com/openvswitch/ovs.git  
#RUN cd ovs  
#8cores ;)  
#RUN DEB_BUILD_OPTIONS='parallel=8' fakeroot debian/rules binary  
RUN dpkg -i /tmp/openvswitch-common*.deb  

