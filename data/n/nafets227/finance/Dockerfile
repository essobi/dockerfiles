FROM pritunl/archlinux  
  
MAINTAINER Stefan Schallenberg aka nafets227 <infos@nafets.de>  
LABEL Description="Finance Container"  
  
VOLUME /finance  
  
RUN \  
pacman -S --needed --noconfirm \  
aqbanking \  
autoconf \  
automake \  
gcc \  
intltool \  
make \  
mariadb-clients \  
s-nail \  
&& \  
paccache -r -k0 && \  
rm -rf /usr/share/man/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
RUN \  
echo /usr/local/lib >/etc/ld.so.conf.d/finance.conf  
  
RUN \  
useradd -d /finance -U finance  
  
# download, compile and install pxlib, a paradox DB library  
RUN \  
cd /finance && \  
curl -L http://downloads.sourceforge.net/sourceforge/pxlib/pxlib-0.6.6.tar.gz
| tar xvz && \  
cd pxlib-0.6.6 && \  
touch config.rpath && \  
autoreconf && \  
./configure --prefix=/usr/local \  
\--with-gsf \  
\--disable-static && \  
make install && \  
ldconfig && \  
cd /finance && \  
rm -rf /finance/pxlib-0.6.6  
  
# copy, compile and install fntxt2sql  
RUN \  
mkdir /tmp/fntxt2sql  
  
COPY fntxt2sql/* /tmp/fntxt2sql/  
  
RUN \  
cd /tmp/fntxt2sql && \  
make && \  
cp -a fntxt2sql /usr/local/bin/fntxt2sql && \  
rm -rf /tmp/fntxt2sql  
  
# copy and install additional scripts  
COPY finance-root-wrapper finance-entrypoint /usr/local/bin/  
RUN \  
chown root:root /usr/local/bin/* && \  
chmod 755 /usr/local/bin/*  
  
ENTRYPOINT [ "/usr/local/bin/finance-root-wrapper" ]  
  

