FROM debian:wheezy  
MAINTAINER Leandro David Cacciagioni <leandro.21.2008@gmail.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get dist-upgrade -qqy --force-yes && \  
apt-get install -qqy --force-yes wget ca-certificates procps default-jre-
headless libwxbase2.8-0 libwxgtk2.8-0 && \  
mkdir /erlang && \  
wget http://packages.erlang-solutions.com/site/esl/esl-
erlang/FLAVOUR_1_general/esl-erlang_17.5.3-1~debian~wheezy_amd64.deb -O
/erlang/erlang.deb && \  
dpkg -i --ignore-depends=esl-erlang /erlang/erlang.deb && \  
apt-get install -qqyf && \  
rm -rf /erlang && apt-get autoremove -qqy && \  
apt-get clean && apt-get autoclean && \  
rm -rf /usr/share/man/?? && rm -rf /usr/share/man/??_*  
  
CMD erl  

