FROM debian:jessie  
  
MAINTAINER Derek Slager <derekslager@gmail.com>  
  
RUN apt-get update && apt-get -y install curl bzip2 g++ libgettextpo0 gettext
automake autoconf file make libtool  
  
ADD install-mono.sh /tmp/install-mono.sh  
  
RUN /tmp/install-mono.sh  
  
RUN rm /tmp/install-mono.sh  
  
RUN mozroots --import --sync  

