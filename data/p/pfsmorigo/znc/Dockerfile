FROM debian:latest  
MAINTAINER Paulo Flabiano Smorigo <pfsmorigo@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y build-essential libssl-dev libperl-dev wget \  
&& cd /usr/local/src \  
&& wget -O- http://znc.in/releases/znc-latest.tar.gz | tar xz \  
&& cd znc-* \  
&& wget https://raw.githubusercontent.com/jpnurmi/znc-
clientbuffer/master/clientbuffer.cpp -O ./modules/clientbuffer.cpp \  
&& ./configure \--with-openssl \  
&& make \  
&& make install \  
&& useradd -m -s /bin/bash -d /var/lib/znc znc \  
&& apt-get -y remove build-essential wget \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/* /usr/local/src/*  
  
USER znc  
ENTRYPOINT /usr/local/bin/znc --datadir /var/lib/znc \--foreground  

