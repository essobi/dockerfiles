FROM debian:jessie  
MAINTAINER Daniel Guerra  
RUN apt-get -yy update  
RUN apt-get -yy install curl debootstrap  
RUN apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6  
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >>
/etc/apt/sources.list  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get -y autoremove &&
apt-get clean  
CMD /bin/bash  

