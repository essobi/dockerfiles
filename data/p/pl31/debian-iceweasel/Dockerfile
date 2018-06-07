FROM pl31/debian:stretch  
MAINTAINER Patrick Büch <dh@paco.pl31.de>  
  
# install services  
RUN echo "Europe/Berlin" > /etc/timezone && \  
dpkg-reconfigure tzdata && \  
apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install \  
iceweasel \  
iceweasel-adblock-plus  
  
# run new iceweasel session  
ENTRYPOINT ["iceweasel", "-no-remote"]  

