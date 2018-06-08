FROM pashi/arch  
MAINTAINER Pasi Lammi <pasi.lammi@iki.fi>  
  
RUN pacman -S collectd net-snmp --noconfirm  
RUN mkdir /app  
RUN mv /etc/collectd.conf /etc/collectd.conf.orig  
RUN ln -s /app/collectd.conf /etc/collectd.conf  
VOLUME /app  
CMD /usr/sbin/collectd -f  

