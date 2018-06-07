FROM ubuntu:xenial  
MAINTAINER Heiko Bornholdt "heiko@bornholdt.it"  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& \  
apt-get update \  
&& \  
apt-get install -y \  
icinga \  
nagios-nrpe-plugin \  
libnet-dns-perl \  
curl \  
&& \  
apt-get clean \  
&& \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN dpkg-statoverride --update --add nagios www-data 2710 /var/lib/icinga/rw/
\  
&& \  
dpkg-statoverride --update --add nagios nagios 751 /var/lib/icinga/  
#RUN mkdir /var/run/munin \  
# && \  
# chown munin:munin /var/run/munin  
  
ADD docker/run.sh /run.sh  
ADD docker/check_live_snds /usr/lib/nagios/plugins/check_live_snds  
ADD docker/prowl.pl /usr/local/bin/prowl.pl  
  
VOLUME /etc/postfix/  
VOLUME /etc/icinga/  
VOLUME /var/lib/icinga/  
VOLUME /var/cache/icinga  
  
EXPOSE 80  
  
CMD ["/run.sh"]  

