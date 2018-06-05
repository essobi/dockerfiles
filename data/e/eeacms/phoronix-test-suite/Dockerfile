FROM ubuntu:trusty  
MAINTAINER Antonio De Marinis <demarinis@eea.europa.eu>  
  
RUN apt-get update \  
&& apt-get -y install \  
build-essential wget unzip perl perl-base perl-modules libsdl-perl \  
libperl-dev libpcre3-dev mesa-utils php5-cli php5-gd php5-json zlib1g-dev
libpng-dev sqlite \  
&& cd /tmp \  
&& wget http://phoronix-test-
suite.com/releases/repo/pts.debian/files/phoronix-test-suite_6.2.1_all.deb \  
&& dpkg -i phoronix-test-suite_6.2.1_all.deb \  
&& rm -f phoronix-test-suite_6.2.1_all.deb  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
ENTRYPOINT /run.sh  

