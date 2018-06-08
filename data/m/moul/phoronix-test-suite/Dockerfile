FROM ubuntu:quantal  
MAINTAINER Manfred Touron m@42.am  
  
RUN apt-get update  
RUN apt-get -y install build-essential wget unzip  
RUN apt-get -y install perl perl-base perl-modules libsdl-perl libperl-dev
libpcre3-dev mesa-utils  
RUN apt-get -y install php5-cli php5-gd php5-json  
RUN cd /tmp; wget http://phoronix-test-
suite.com/releases/repo/pts.debian/files/phoronix-test-suite_4.8.5_all.deb  
RUN cd /tmp; dpkg -i phoronix-test-suite_4.8.5_all.deb  
RUN cd /tmp; rm -f phoronix-test-suite_4.8.5_all.deb  
  
ENTRYPOINT ["phoronix-test-suite"]  

