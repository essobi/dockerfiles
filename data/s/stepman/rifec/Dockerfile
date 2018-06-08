FROM ubuntu:trusty  
MAINTAINER schinken <schinken@hackerspace-bamberg.de>  
  
RUN apt-get -q update  
RUN apt-get -y install git-core  
RUN apt-get -y install libconfig-inifiles-perl libwww-perl libdigest-md5-perl
libparams-validate-perl libproc-daemon-perl libxml-simple-perl  
  
RUN git clone https://github.com/kristofg/rifec.git /usr/local/src/rifec  
  
ADD rifec.config /usr/local/src/rifec/rifec.config  
  
ADD run.sh /usr/local/src/rifec/run.sh  
RUN chmod +x /usr/local/src/rifec/run.sh  
  
EXPOSE 59278  
VOLUME ["/mnt/pictures"]  
ENTRYPOINT /usr/local/src/rifec/run.sh  

