FROM ubuntu:13.10  
MAINTAINER Viktor Miroshnikov <viktor@flowhealth.com>  
  
RUN apt-get -q update  
RUN apt-get -q -y install libexpat1-dev gcc build-essential ncurses-dev
libssl-dev autoconf libpam0g-dev make git libsctp1  
ADD erlang-R16B03.deb /usr/local/share/erlang-r16b03.deb  
RUN dpkg -i /usr/local/share/erlang-r16b03.deb  

