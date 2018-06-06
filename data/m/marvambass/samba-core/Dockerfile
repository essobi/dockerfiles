FROM ubuntu:16.04  
  
ENV samba_version 4.6.4  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q -y update && \  
apt-get -q -y install build-essential \  
wget && \  
apt-get -q -y install acl \  
attr \  
autoconf \  
bison \  
build-essential \  
debhelper \  
dnsutils \  
docbook-xml \  
docbook-xsl \  
flex \  
gdb \  
krb5-user \  
libacl1-dev \  
libaio-dev \  
libattr1-dev \  
libblkid-dev \  
libbsd-dev \  
libcap-dev \  
libcups2-dev \  
libgnutls-dev \  
libjson-perl \  
libldap2-dev \  
libncurses5-dev \  
libpam0g-dev \  
libparse-yapp-perl \  
libpopt-dev \  
libreadline-dev \  
perl \  
perl-modules \  
pkg-config \  
python-all-dev \  
python-dev \  
python-dnspython \  
python-crypto \  
xsltproc \  
zlib1g-dev  
  
RUN wget
https://download.samba.org/pub/samba/stable/samba-${samba_version}.tar.gz && \  
tar xvf samba-${samba_version}.tar.gz && \  
rm samba-${samba_version}.tar.gz && \  
cd samba-${samba_version} && \  
./configure && \  
make && \  
make install && \  
cp examples/smb.conf.default /usr/local/samba/etc/smb.conf && \  
cd - && \  
rm -rf samba-${samba_version}  
  
EXPOSE 139 445  
  
CMD [ "/usr/local/samba/sbin/smbd", "-F", "-S" ]  

