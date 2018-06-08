FROM ubuntu:14.04  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN ln -s -f /bin/true /usr/bin/chfn  
RUN apt-get -y install git man lynx emacs wget  
ADD .emacs .emacs  
RUN apt-get -y install build-essential libncurses5-dev openssl libssl-dev
libxml2-utils fop xsltproc unixodbc-dev autoconf openjdk-7-jdk  
RUN apt-get -y install libwxbase2.8 libwxgtk2.8-dev libqt4-opengl-dev  
RUN git clone https://github.com/erlang/otp.git  
RUN cd otp && git checkout OTP-17.2.1 && /otp/otp_build autoconf &&
./configure && make && make install-docs && make install  
RUN git clone git://github.com/rebar/rebar.git && cd rebar && git checkout
2.5.1 && ./bootstrap  
RUN ln -s /rebar/rebar /usr/local/bin/  

