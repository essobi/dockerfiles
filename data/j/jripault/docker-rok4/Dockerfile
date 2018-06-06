FROM debian:jessie  
MAINTAINER jripault  
  
RUN apt-get update && apt-get install -y wget unzip libreadline-dev
libncurses5-dev libpcre3-dev libssl-dev libpq-dev perl libexpat-dev make
build-essential gettext nasm automake perl libxml2-dev libgdal-perl liblog-
log4perl-perl libconfig-inifiles-perl libxml-libxml-simple-perl libfile-copy-
link-perl cmake  
  
RUN wget http://www.rok4.org/data/src/rok4-0.25.4-src.zip && unzip
rok4-0.25.4-src.zip  
  
RUN cd rok4-0.25.4 && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install && \  
rm -rf ../rok4-0.25.4-src.zip

