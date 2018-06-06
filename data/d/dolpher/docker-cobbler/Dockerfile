FROM ubuntu:14.04.4  
MAINTAINER dolpher.du@intel.com  
  
RUN apt-get update \  
&& apt-get install -y cobbler cobbler-web dnsmasq supervisor \  
&& apt-get clean  
  
ADD conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD conf/dnsmasq.template /etc/cobbler/dnsmasq.template  
RUN (echo -n "cobbler:Cobbler:" && echo -n "cobbler:Cobbler:cobbler" | md5sum
| awk '{print $1}') > /etc/cobbler/users.digest  
RUN sed -i "s/^manage_dhcp: .*$/manage_dhcp: 1/" /etc/cobbler/settings  
RUN sed -i "s/^manage_dns: .*$/manage_dns: 1/" /etc/cobbler/settings  
RUN sed -i "s/^module = manage_bind/module = manage_dnsmasq/"
/etc/cobbler/modules.conf  
RUN sed -i "s/^module = manage_isc/module = manage_dnsmasq/"
/etc/cobbler/modules.conf  
  
ADD init-cobbler /usr/local/bin/init-cobbler  
CMD ["init-cobbler"]  
  
EXPOSE 25151  
EXPOSE 53/udp  
EXPOSE 69/udp  
EXPOSE 80  
EXPOSE 443  

