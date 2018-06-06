FROM ubuntu:latest  
MAINTAINER tuannvm@mail.ru  
RUN apt-get update && \  
apt-get install pure-ftpd openssl libpam-dev libcap2-dev libldap2-dev
libmysqlclient-dev libmysqlclient15-dev libpq-dev libssl-dev po-debconf dpkg-
dev debhelper -y  
RUN mkdir /tmp/pure-ftpd/ && \  
cd /tmp/pure-ftpd/ && \  
apt-get source pure-ftpd && \  
cd pure-ftpd-* && \  
sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules && \  
dpkg-buildpackage -b -uc  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd-common*.deb  
RUN apt-get -y install openbsd-inetd  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd_*.deb  
RUN apt-mark hold pure-ftpd pure-ftpd-common  
RUN cd /etc/pure-ftpd && \  
mkdir /home/ftp && \  
chown www-data:www-data -R /home/ftp && \  
echo yes > ./conf/ChrootEveryone && \  
echo yes > ./conf/DontResolve && \  
echo yes > ./conf/NoChmod && \  
echo yes > ./conf/ProhibitDotFilesWrite && \  
echo yes > ./conf/CustomerProof && \  
echo '20000 20099' > ./conf/PassivePortRange && \  
echo ',21' > ./conf/Bind && \  
echo '2' > ./conf/TLS && \  
openssl req -x509 -nodes -newkey rsa:1024 -keyout /etc/ssl/private/pure-
ftpd.pem -out /etc/ssl/private/pure-ftpd.pem -subj
"/C=VN/ST=South/L=HCM/O=TCorp/OU=IT Department/CN=ftp.tuannvm.com"  
ADD pureftpd.passwd /etc/pure-ftpd/  
ADD pure-ftpd /etc/init.d/  
RUN pure-pw mkdb  
RUN ln -sf /dev/stdout /var/log/pure-ftpd/transfer.log  
CMD /usr/sbin/pure-ftpd -l puredb:/etc/pure-ftpd/pureftpd.pdb -x -u 30 -H -S
,21 -O clf:/var/log/pure-ftpd/transfer.log -Z -A -p 20000:20099 -E -R -8 UTF-8
-Y 2  
EXPOSE 21/tcp 20000-20099/tcp  

