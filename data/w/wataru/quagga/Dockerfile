# quagga  
#  
FROM ubuntu:14.04  
MAINTAINER ISHIDA Wataru <ishida.wataru@lab.ntt.co.jp>  
  
RUN useradd -M quagga  
RUN mkdir /var/log/quagga && chown quagga:quagga /var/log/quagga  
RUN mkdir /var/run/quagga && chown quagga:quagga /var/run/quagga  
RUN apt-get update && \  
apt-get install -qy wget unzip autoconf libtool gawk make supervisor telnet  
RUN wget --no-check-certificate
https://github.com/ishidawataru/quagga/archive/master.zip && \  
unzip master.zip && \  
(cd quagga-master && \  
./bootstrap.sh && \  
./configure --disable-doc --localstatedir=/var/run/quagga --enable-fpm && \  
make && make install)  
RUN ldconfig  
ADD zebra.conf /usr/local/etc/zebra.conf  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENTRYPOINT ["/usr/bin/supervisord"]  

