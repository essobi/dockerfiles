FROM ubuntu:xenial  
  
# add user nagios  
RUN useradd nagios -d /var/lib/nagios  
  
  
RUN apt-get update -y && \  
apt-get install -y build-essential libssl-dev nagios-plugins nagios-nrpe-
server wget && \  
wget http://archive.ubuntu.com/ubuntu/pool/main/n/nagios-nrpe/nagios-
nrpe_2.15.orig.tar.gz && \  
tar xzf nagios-nrpe_2.15.orig.tar.gz && cd /nrpe-2.15 && \  
./configure \  
\--prefix=/usr \  
\--enable-ssl \  
\--with-ssl-lib=/usr/lib/x86_64-linux-gnu \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--libexecdir=/usr/lib/nagios/plugins \  
\--libdir=/usr/lib/nagios \  
\--enable-command-args && \  
make && make install && rm /usr/sbin/nrpe && \  
ln -s /usr/bin/nrpe /usr/sbin/nrpe && \  
wget https://github.com/craig-
willis/check_kube/releases/download/v0.1/check_kube-linux-amd64 -O
/usr/lib/nagios/plugins/check_kube && \  
chmod +x /usr/lib/nagios/plugins/check_kube && \  
apt-get remove -y libssl-dev wget && rm -r /nrpe-2.15 && rm /nagios-
nrpe_2.15.orig.tar.gz  
  
  
EXPOSE 5666  
  
COPY plugins/* /usr/lib/nagios/plugins/  
COPY nrpe.cfg /etc/nagios/nrpe.cfg  
COPY nrpe-entrypoint.sh /nrpe-entrypoint.sh  
ENTRYPOINT ["/nrpe-entrypoint.sh"]  
CMD ["nrpe"]  

