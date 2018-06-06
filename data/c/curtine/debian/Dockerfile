FROM debian:8  
  
RUN apt -y update &&\  
apt -y upgrade &&\  
apt -y install gcc\  
g++\  
cmake\  
vim\  
dmidecode\  
libcurl3\  
perl\  
liburi-perl\  
libproc-processtable-perl\  
libfile-slurp-perl\  
libhttp-message-perl\  
libjson-perl\  
libwww-perl\  
libipc-run-perl\  
libconvert-asn1-perl\  
libsocket6-perl\  
apt-transport-https\  
bind9-host\  
dnsutils\  
lsb-release\  
libconfig-std-perl\  
automake\  
libtool-bin\  
pkg-config\  
make\  
libssl-dev\  
libcurl4-openssl-dev\  
dpkg-dev\  
wget\  
gettext\  
sudo\  
net-tools\  
clang\  
silversearcher-ag\  
ccache\  
libpam0g-dev\  
libboost-dev\  
attr\  
cppcheck\  
chkconfig\  
openssh-server\  
uuid-runtime\  
curl &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN cd /tmp &&\  
wget http://ftp.br.debian.org/debian/pool/main/libh/libhttp-daemon-ssl-
perl/libhttp-daemon-ssl-perl_1.04-3_all.deb &&\  
dpkg -i libhttp-daemon-ssl-perl_1.04-3_all.deb &&\  
rm -f libhttp-daemon-ssl-perl_1.04-3_all.deb  
RUN cd /tmp &&\  
wget http://www.kernel.org/pub/software/scm/git/git-2.7.4.tar.gz &&\  
tar xf git-2.7.4.tar.gz &&\  
cd /tmp/git-2.7.4 &&\  
make -j3 configure &&\  
./configure --prefix=/usr &&\  
make -j3 &&\  
make -j3 install &&\  
rm -rf /tmp/git-2.7.4*  
RUN cd /tmp &&\  
wget https://dev.mysql.com/get/Downloads/Connector-C++/mysql-
connector-c++-1.1.9-linux-debian8-x86-64bit.tar.gz &&\  
tar xf mysql-connector-c++-1.1.9-linux-debian8-x86-64bit.tar.gz &&\  
cd /tmp/mysql-connector-c++-1.1.9-linux-debian8-x86-64bit &&\  
cp -r include /usr/ &&\  
mv lib/libmysqlcppconn.so* /usr/lib/ &&\  
rm -rf /tmp/mysql-connector-c++-1.1.9-linux-debian8-x86-64bit*  
  

