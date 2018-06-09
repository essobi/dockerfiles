# Face recognizer  
FROM ubuntu:trusty  
MAINTAINER Daniele Giglio <giglio.d@gmail.com>  
RUN apt-get update  
RUN apt-get -y install openssh-server && mkdir /var/run/sshd  
#RUN apt-get -y install vim git zip bzip2 fontconfig curl  
RUN apt-get -y install supervisor  
RUN apt-get -y install build-essential make gettext  
RUN apt-get -y install checkinstall  
RUN apt-get -y install autoconf automake libtool  
# required to compile asterisk  
RUN apt-get -y install libncurses5-dev uuid-dev libjansson-dev libxml2-dev
libsqlite3-dev libspeex-dev  
RUN apt-get install -yqq inetutils-ping net-tools  
RUN apt-get -y install libpri-dev  
  
# Install Asterisk  
ENV AST_AR asterisk-current.tar.gz  
ENV AST_SRCDIR asterisk-src  
## downloads  
RUN cd  
WORKDIR /tmp  
RUN wget
http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-13-current.tar.gz
-O /tmp/$AST_AR  
RUN mkdir $AST_SRCDIR  
RUN tar xzf $AST_AR -C $AST_SRCDIR \--strip-components=1  
# RUN cd asterisk-src  
WORKDIR /tmp/asterisk-src  
  
# compiles  
RUN sh ./configure  
RUN make  
  
# install  
RUN make install  
RUN make samples  
  
ADD asterisk.conf /etc/asterisk/  
ADD extensions.conf /etc/asterisk/  
ADD http.conf /etc/asterisk/  
ADD manager.conf /etc/asterisk/  
ADD sip.conf /etc/asterisk/  
ADD users.conf /etc/asterisk/  
ADD ari.conf /etc/asterisk/  
  
ADD install-asterisk-gui.sh /usr/local/bin/  
  
RUN install-asterisk-gui.sh  
  
EXPOSE 22  
EXPOSE 8088  
EXPOSE 5060  
#RUN service asterisk start  

