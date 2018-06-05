FROM ubuntu:12.04  
MAINTAINER info@abroweb.ru  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y && apt-get clean  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y build-essential wget libssl-dev ncurses-dev libxml2-dev
libsqlite3-dev  
  
RUN cd /usr/src && wget
http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-11-current.tar.gz
&& tar zxvf asterisk* && rm asterisk-11-current.tar.gz  
  
RUN cd /usr/src/asterisk* && ./configure && make menuselect.makeopts && make
&& make install  
  
RUN apt-get install -y python-software-properties supervisor  
RUN apt-get install -y openssh-server htop mc nano  
  
ADD ./resources/install /root/install  
RUN chmod 755 /root/install && /root/install  
  
CMD ["/usr/bin/supervisord", "-n"]  
  
#
https://wiki.asterisk.org/wiki/display/AST/Using+Menuselect+to+Select+Asterisk+Options

