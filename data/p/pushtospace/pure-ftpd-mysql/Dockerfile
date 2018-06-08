FROM pushtospace/ubuntu  
  
MAINTAINER Gino Jongenelen <g.jongenelen@pushto.space>  
  
ADD ./start.sh /root  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y --force-yes install dpkg-dev debhelper wget redis-tools python && \  
apt-get -y build-dep pure-ftpd-mysql && \  
mkdir /ftpdata && \  
mkdir /tmp/pure-ftpd-mysql && \  
cd /tmp/pure-ftpd-mysql && \  
apt-get source pure-ftpd-mysql && \  
cd pure-ftpd-* && \  
sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules && \  
dpkg-buildpackage -b -uc && \  
dpkg -i /tmp/pure-ftpd-mysql/pure-ftpd-common*.deb && \  
apt-get -y install openbsd-inetd && \  
dpkg -i /tmp/pure-ftpd-mysql/pure-ftpd-mysql*.deb && \  
apt-mark hold pure-ftpd pure-ftpd-mysql pure-ftpd-common && \  
groupadd -g 2001 ftpgroup && \  
useradd -u 2001 -g ftpgroup -d /dev/null -s /etc ftpuser && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
echo "50000 50400" > /etc/pure-ftpd/conf/PassivePortRange && \  
chmod +x /root/start.sh  
  
EXPOSE 20 21 50000-50400  
  
ADD ./pureftpd-mysql.conf /etc/pure-ftpd/db  
CMD /root/start.sh

