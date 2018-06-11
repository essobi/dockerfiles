FROM centos:centos7  
  
MAINTAINER Gary Hai "gary@XL59.com"  
RUN yum -y update  
RUN yum -y install tar gcc make  
  
RUN mkdir -p /usr/local/src;\  
cd /usr/local/src;\  
curl https://download.libsodium.org/libsodium/releases/libsodium-1.0.0.tar.gz
| tar xz;\  
cd libsodium*;\  
./configure;\  
make && make check;\  
make install  
  
RUN echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf;\  
ldconfig;  
  
RUN mkdir -p /usr/local/src;\  
cd /usr/local/src;\  
curl http://download.dnscrypt.org/dnscrypt-proxy/dnscrypt-proxy-1.4.1.tar.gz |
tar xz;\  
cd dnscrypt-proxy*;\  
./configure && make;\  
make install  
  
RUN yum -y install unbound  
RUN /usr/sbin/unbound-control-setup -d /etc/unbound/  
ADD server.conf /etc/unbound/local.d/server.conf  
  
# Port of unbound  
EXPOSE 53  
EXPOSE 53/udp  
  
# Port of dnscrypt-proxy  
EXPOSE 40  
EXPOSE 40/udp  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  

