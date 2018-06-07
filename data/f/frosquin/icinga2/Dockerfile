# Icinga2 Docker file  
FROM ubuntu:14.04  
MAINTAINER Frank Rosquin <frank.rosquin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV APT_OPTIONS "-y --no-install-recommends --no-install-suggests -q"  
RUN apt-get update \  
&& apt-get $APT_OPTIONS install wget \  
&& wget -O - http://packages.icinga.org/icinga.key | apt-key add - \  
&& echo "deb http://packages.icinga.org/ubuntu icinga-trusty main" >
/etc/apt/sources.list.d/icinga.list \  
&& echo "deb-src http://packages.icinga.org/ubuntu icinga-trusty main" >>
/etc/apt/sources.list.d/icinga.list \  
&& apt-get update  
  
RUN apt-get $APT_OPTIONS install \  
icinga2 \  
nagios-plugins nagios-snmp-plugins nagios-plugins-contrib \  
libnagios-object-perl libnagios-plugin-perl \  
libtimedate-perl liblwp-useragent-determined-perl libipc-run-perl \  
libswitch-perl \  
snmp nagios-snmp-plugins libnet-snmp-perl python \  
freeipmi-tools whois dnsutils \  
openssl ca-certificates \  
&& apt-get $APT_OPTIONS install icinga2-ido-mysql \  
&& apt-get $APT_OPTIONS install icinga2-ido-pgsql \  
&& apt-get purge -y -q --auto-remove gcc make wget  
  
## Fixes for broken software...  
# .1.3.6.1.2.1.2.2.1.2 gives ifDescription, we need ifName  
RUN sed -i -e "s/my \$descr_table = '1.3.6.1.2.1.2.2.1.2';/my \$descr_table =
'1.3.6.1.2.1.31.1.1.1.1';/g" /usr/lib/nagios/plugins/check_snmp_int.pl  
  
ADD conf/icinga2.conf /etc/icinga2/icinga2.conf  
ADD scripts/pusher.py /etc/icinga2/scripts/pusher.py  
RUN chmod 755 /etc/icinga2/scripts/pusher.py  
  
RUN icinga2 feature enable command  
  
RUN mkdir -p /run/icinga2/cmd  
RUN chown -R nagios:nagios /run/icinga2  
ADD icinga2.sh /icinga2.sh  
RUN chmod 755 /icinga2.sh  
  
ENTRYPOINT ["/icinga2.sh"]  

