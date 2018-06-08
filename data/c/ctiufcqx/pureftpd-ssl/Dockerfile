FROM debian:jessie  
MAINTAINER Coordenadoria de Tecnologia da Informação <ccti@quixada.ufc.br>  
  
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
  
# INSTALL AND CONFIGURE OPENSSL  
RUN apt-get install openssl ssl-cert -y  
RUN openssl req -x509 -nodes -days 7300 -newkey rsa:2048 -keyout
/etc/ssl/private/pure-ftpd.pem -out /etc/ssl/private/pure-ftpd.pem -subj
"/C=BR/ST=Ceara/L=Quixada/O=UFC Quixada/OU=CTI/CN=ftpsites.quixada.ufc.br"  
  
# setup ftpgroup and ftpuser  
RUN groupadd ftpgroup  
RUN useradd -g ftpgroup -d /home/ftpusers -s /dev/null ftpuser  
  
VOLUME /home/ftpusers  
  
# startup  
#CMD /usr/sbin/pure-ftpd -c 50 -C 10 -l puredb:/etc/pure-ftpd/pureftpd.pdb -E
-j -R -p 30000:30009  
EXPOSE 21 40000:40100  
# startup  
CMD /usr/sbin/pure-ftpd -c 50 -C 10 -l puredb:/etc/pure-ftpd/pureftpd.pdb -E
-i -A -8 UTF-8 -j -R -u 1000 -p 40000:40100 -Y 2  
  
# PARAMETERS  
# https://download.pureftpd.org/pub/pure-ftpd/doc/README  
# -1 --logpid <file>  
# c --maxclientsnumber <number>  
# -C --maxclientsperip <number>  
# -E --noanonymous  
# -i --anonymouscantupload  
# -A --chrooteveryone  
# -8 --fscharset <charset>  
# -j --createhomedir  
# -u --minuid <uid>  
# -p --passiveportrange <minport:maxport>  
# -Y --tls <0:no TLS | 1:TLS+cleartext | 2:enforce TLS |  
# 3: enforce encrypted data channel as well>  

