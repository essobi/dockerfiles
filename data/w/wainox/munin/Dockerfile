FROM ubuntu:xenial  
MAINTAINER Heiko Bornholdt "heiko@bornholdt.it"  
# libcgi-pm-perl: Für die ganz großen Graphen brauchen wir CGI/Fast.pm. Das
Paket wird nicht automatisch mit installiert.  
RUN apt-get update \  
&& \  
apt-get install -y \  
apache2 \  
munin \  
libcgi-pm-perl \  
&& \  
apt-get clean \  
&& \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /var/run/munin \  
&& \  
chown munin:munin /var/run/munin  
  
ADD docker/run.sh /run.sh  
  
VOLUME /etc/munin  
VOLUME /var/lib/munin  
  
EXPOSE 80  
CMD ["/run.sh"]  

