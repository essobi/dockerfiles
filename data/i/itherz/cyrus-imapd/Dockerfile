FROM debian:latest  
  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
RUN cd /opt && apt update -y && \  
apt install -y wget autoconf libtool pkg-config libdb5.3++-dev libssl-dev
libsasl2-dev libldap2-dev libmysql++-dev libpcre++-dev libjansson-dev
libevent-dev make sasl2-bin bison flex git g++  
  
#install libtool 2.4.6 for sqlite3 build  
RUN cd /opt && wget
http://ftp.ru.debian.org/debian/pool/main/libt/libtool/libtool_2.4.6-2_all.deb
&& dpkg -i libtool* && \  
wget http://www.sqlite.org/2016/sqlite-autoconf-3150100.tar.gz && tar xzvpf
sqlite* && rm *.tar.gz && cd sqlite* && autoreconf -vi && ./configure
\--enable-session \--enable-json1 \--enable-fts5 && make && make install && \  
apt install -y libicu-dev libc6-dev build-essential cmake libxml2-dev
libglib2.0-dev  
  
#install ical  
RUN cd /opt && git clone https://github.com/libical/libical && cd libical &&
mkdir build && cd build && cmake .. && make && make install && cd ../.. && rm
-rf libical && \  
cd /opt && wget ftp://ftp.cyrusimap.org/cyrus-imapd/cyrus-
imapd-3.0.0-beta4.tar.gz && tar xzvpf cyrus* && rm *.tar.gz  
  
RUN cd /opt/cyrus* && autoreconf -vi && ./configure \--enable-backup \--with-
sqlite=/usr/local \--with-zephyr \--with-sasl \--enable-autocreate \--enable-
idled \--enable-gssapi \--enable-event-notifications \--with-mysql \--with-
ldap \--with-cyrus-user=cyrus \--with-cyrus-group=mail \--prefix=/usr \--exec-
prefix=/usr \--libexecdir=/usr/libexec \--sysconfdir=/etc
\--localstatedir=/var \--with-ical=/usr/local && \  
make && make install && useradd -g mail cyrus && mkdir -p /var/run/cyrus/proc
&& chmod 777 -R /var/run/cyrus/proc && \  
mkdir -p /var/lib/cyrus && chown cyrus -R /var/lib/cyrus && mkdir -p
/var/imap/db && chmod 777 -R /var/imap/db && mkdir -p /var/mail && chown cyrus
-R /var/mail && \  
mkdir -p /var/spool/cyrus/news && mkdir -p /var/spool/news && chown cyrus -R
/var/spool/cyrus/news && chown cyrus -R /var/spool/news && mkdir -p
/var/spool/sieve && chown cyrus -R /var/spool/sieve && \  
cp /opt/cyrus*/master/conf/normal.conf /etc/cyrus.conf && \  
ldconfig && usermod -a -G mail,sasl cyrus  
  
ADD imapd.sh /opt/imapd.sh  
  
RUN chmod +x /opt/imapd.sh && apt install -y uuid-dev libgcrypt-dev libestr-
dev flex dh-autoreconf bison python-docutils libxml2-dev git python-setuptools
re2c && \  
cd /opt && git clone https://github.com/rsyslog/libfastjson && cd libfastjson
&& autoreconf -v \--install && ./configure && make && make install && \  
git clone https://github.com/rsyslog/liblogging && cd liblogging && autoreconf
-v \--install && ./configure \--disable-man-pages && make && make install && \  
git clone https://github.com/rsyslog/rsyslog && cd rsyslog && ./autogen.sh
\--enable-omstdout && make && make install && ldconfig && \  
mkdir /var/log/supervisor/ && /usr/bin/easy_install supervisor &&
/usr/bin/easy_install supervisor-stdout  
  
EXPOSE 110 143 993 995 4190  
  
ADD supervisord.conf /etc/supervisord.conf  
ADD rsyslog.conf /etc/rsyslog.conf  
  
CMD ["supervisord","-n","-c","/etc/supervisord.conf"]  

