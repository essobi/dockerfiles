FROM ubuntu:14.04  
MAINTAINER Jean-Pierre PRUNARET <jean-pierre+git@prunetwortk.fr>  
  
RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q &&
apt-get -y -q autoclean && apt-get -y -q autoremove)  
## engine dependencies  
RUN apt-get -y install build-essential libfile-slurp-perl libjson-perl
liblist-moreutils-perl libio-socket-inet6-perl libmodule-find-perl libmoose-
perl libfile-sharedir-perl libhash-merge-perl libreadonly-perl libmail-
rfc822-address-perl libintl-xs-perl libssl-dev libdevel-checklib-perl libtest-
fatal-perl libtie-simple-perl libio-capture-perl libgeography-countries-perl
libidn11-dev  
## cli dependencies  
RUN apt-get -y install libmoosex-getopt-perl libtext-reflow-perl libmodule-
install-perl  
  
  
## install engine  
RUN perl -MCPAN -e 'install Zonemaster'  
## install cli  
RUN perl -MCPAN -e 'install Zonemaster::CLI'  

