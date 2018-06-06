FROM debian:jessie  
MAINTAINER github.com/mikeybot  
  
# properly setup debian sources  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "deb http://http.debian.net/debian jessie main\n\  
deb-src http://http.debian.net/debian jessie main\n\  
deb http://http.debian.net/debian jessie-updates main\n\  
deb-src http://http.debian.net/debian jessie-updates main\n\  
deb http://security.debian.org jessie/updates main\n\  
deb-src http://security.debian.org jessie/updates main\n\  
" > /etc/apt/sources.list  
RUN apt-get -y update  
  
# install package building helpers  
RUN apt-get -y --force-yes install dpkg-dev debhelper  
  
# install dependancies  
RUN apt-get -y build-dep pure-ftpd  
  
# build from source  
RUN mkdir /tmp/pure-ftpd/ && \  
cd /tmp/pure-ftpd/ && \  
apt-get source pure-ftpd && \  
cd pure-ftpd-* && \  
sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules && \  
dpkg-buildpackage -b -uc  
  
# install the new deb files  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd-common*.deb  
RUN apt-get -y install openbsd-inetd  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd_*.deb  
  
# Prevent pure-ftpd upgrading  
RUN apt-mark hold pure-ftpd pure-ftpd-common  
  
#ENV PUBLICHOST ftp.foo.com  
VOLUME /data  
VOLUME /config  
  
# Add user setup script  
ADD setup.sh /root  
  
# Make executable  
RUN chmod +x /root/setup.sh  
  
# startup  
CMD /bin/bash /root/setup.sh && /usr/sbin/pure-ftpd -c 5 -C 10 -l
puredb:/etc/pure-ftpd/pureftpd.pdb -E -j -R  
  
EXPOSE 21  

