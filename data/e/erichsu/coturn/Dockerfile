FROM debian  
MAINTAINER Eric Hsu <erichsu@livemail.tw>  
  
# Set correct environment variables.  
RUN apt-get update  
RUN apt-get install -y gdebi-core curl  
  
ENV COTURN_VER 4.4.5.3  
RUN cd /tmp/ && curl -sL http://turnserver.open-
sys.org/downloads/v${COTURN_VER}/turnserver-${COTURN_VER}-debian-wheezy-
ubuntu-mint-x86-64bits.tar.gz | tar -xzv  
  
RUN groupadd turnserver  
RUN useradd -g turnserver turnserver  
RUN gdebi -n /tmp/coturn*.deb  
  
WORKDIR /opt  
ADD turnserver.sh /opt  
CMD ./turnserver.sh  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

