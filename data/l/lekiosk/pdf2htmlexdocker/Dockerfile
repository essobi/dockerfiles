FROM ubuntu:15.04  
ENV PDF2HTML_VERSION 0.12-1~git201411121058r1a6ec-0ubuntu1~precise1  
ENV FONTFORGE_VERSION 20150612-0ubuntu1~precise  
ENV NODEJS_VERSION 0.10.37-1chl1~precise1  
  
MAINTAINER stephane.ledorze@gmail.com  
  
RUN echo "deb http://us-east-1.ec2.archive.ubuntu.com/ubuntu/ precise
multiverse" >> /etc/apt/sources.list  
RUN echo "deb http://us-east-1.ec2.archive.ubuntu.com/ubuntu/ precise-updates
multiverse" >> /etc/apt/sources.list  
  
# Freshen up ubuntu  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
  
RUN apt-get install -y software-properties-common python-software-properties
apt-utils  
RUN apt-get -y install curl wget  
  
#install fontforge PPA  
#RUN apt-add-repository ppa:fontforge/fontforge  
# install nodeJs PPA  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -  
  
RUN apt-get update  
  
#  
#Install git and all dependencies  
# libtiff4-dev  
RUN apt-get install -y sudo git cmake autotools-dev libjpeg-dev libpng12-dev
libgif-dev libxt-dev autoconf automake libtool bzip2 libxml2-dev
libuninameslist-dev libspiro-dev python-dev libpango1.0-dev libcairo2-dev
chrpath uuid-dev uthash-dev  
  
#  
#Clone the pdf2htmlEX fork of fontforge  
#compile it  
#  
RUN git clone https://github.com/coolwanglu/fontforge.git fontforge.git  
RUN cd fontforge.git && git checkout pdf2htmlEX && ./autogen.sh && ./configure
&& make V=1 && sudo make install  
  
#  
#Install poppler utils  
#  
RUN apt-get install -y libpoppler-glib-dev poppler-utils libpoppler-dev
gir1.2-poppler-0.18 libpoppler-cil-dev libpopplerkit-dev libpoppler-cpp-dev
libpoppler-private-dev  
  
#  
#Install cairo utils  
#  
RUN apt-get install -y libcairo2-dev libghc-svgcairo-dev  
  
#  
#Clone and install the pdf2htmlEX git repo  
#  
RUN git clone git://github.com/coolwanglu/pdf2htmlEX.git  
RUN cd pdf2htmlEX && cmake . && make && sudo make install  
  

