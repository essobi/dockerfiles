From scratch  
MAINTAINER Oskari Rauta <oskari.rauta@gmail.com>  
  
EXPOSE 80  
EXPOSE 22  
ADD files/lede-17.01.4-x86-64-generic-rootfs.tar.gz /  
  
RUN mkdir -pv /var/run  
RUN mkdir -pv /var/lock  
  
RUN sed --in-place '/ip -4 address flush dev $pi_ifname/d'
/lib/preinit/10_indicate_preinit  
RUN sed -i -e 's/# only use the first one/return/g'
/lib/preinit/10_indicate_preinit  
  
RUN opkg update  
RUN opkg install nano  
  
RUN /etc/init.d/dnsmasq disable  
RUN /etc/init.d/done disable  
RUN /etc/init.d/firewall disable  
RUN /etc/init.d/gpio_switch disable  
RUN /etc/init.d/led disable  
RUN /etc/init.d/network disable  
RUN /etc/init.d/odhcpd disable  
RUN /etc/init.d/sysctl disable  
RUN /etc/init.d/sysfixtime disable  
RUN /etc/init.d/sysntpd disable  
  
RUN rm -f /etc/config/network /etc/inittab /bin/sh  
  
COPY files/network /etc/config/network  
COPY files/sh /bin/sh  
COPY files/inittab /etc/inittab  
  
CMD ["/sbin/init"]  

