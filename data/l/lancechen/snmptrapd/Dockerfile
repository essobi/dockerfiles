FROM debian:stable  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl file gcc make
libextutils-makemaker-cpanfile-perl  
  
RUN curl -L -O http://sourceforge.net/projects/net-snmp/files/net-
snmp/5.7.3/net-snmp-5.7.3.tar.gz \  
&& tar xf net-snmp-5.7.3.tar.gz \  
&& cd net-snmp-5.7.3 \  
&& ./configure --prefix=/usr --sysconfdir=/etc --sbindir=/usr/bin
--mandir=/usr/share/man --disable-embedded-perl \  
&& make \  
&& make install  
  
CMD ["snmptrapd", "-f"]  

