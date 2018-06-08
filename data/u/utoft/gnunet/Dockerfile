FROM ubuntu  
MAINTAINER Jesper Utoft <jesper@utoft.org>  
  
COPY release-keys/ release-keys/  
  
RUN gpg \--yes \--always-trust \--import ./release-keys/* \  
&& echo "Defining command" \  
&& getpackage () { /usr/bin/wget $3 -O $2; /usr/bin/wget $3.sig -O $2.sig; gpg
\--verify $2.sig $2; mkdir -p $1; cd $1; tar \--strip-components=1 -xf ../$2;
./configure; make; make install; cd ..; rm -rf $1*; } \  
&& echo "Installing packages" \  
&& apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y
\--no-install-recommends \  
make \  
gcc \  
wget \  
# runtime dependency followed by dev package  
libltdl7 \  
libltdl-dev \  
libbluetooth3 \  
libbluetooth-dev \  
# libmicrohttpd10 \  
# libmicrohttpd-dev \  
libunbound2 \  
libunbound-dev \  
libsqlite3-0 \  
libsqlite3-dev \  
libmysqlclient20 \  
libmysqlclient-dev \  
libp11-kit0 \  
libp11-kit-dev \  
libgpg-error0 \  
libgpg-error-dev \  
libunistring0 \  
libunistring-dev \  
libidn11 \  
libidn11-dev \  
libglpk36 \  
libglpk-dev \  
libextractor3 \  
libextractor-dev \  
# gstreamer1.0 libgstreamer1.0-0 \  
# libgstreamer1.0-dev \  
# libpulse-mainloop-glib0 libpulse0 \  
# libpulse-dev \  
# libopus0 \  
# libopus-dev \  
&& LIBGCRYPT=1.6.0 \  
&& getpackage libgcrypt libgcrypt.tar.gz
ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-$LIBGCRYPT.tar.gz \  
&& NETTLE=3.2 \  
&& getpackage nettle nettle.tar.gz
ftp://ftp.gnu.org/gnu/nettle/nettle-$NETTLE.tar.gz \  
&& LIBTASN1=4.9 \  
&& getpackage libtasn1 libtasn1.tar.gz
ftp://ftp.gnu.org/gnu/libtasn1/libtasn1-$LIBTASN1.tar.gz \  
&& P11KIT=0.23.2 \  
&& getpackage p11-kit p11-kit.tar.gz
https://p11-glue.freedesktop.org/releases/p11-kit-$P11KIT.tar.gz \  
&& GNUTLS_MAJOR=v3.4 \  
&& GNUTLS_MINOR=3.4.15 \  
&& getpackage gnutls gnutls.tar.xz
ftp://ftp.gnupg.org/gcrypt/gnutls/$GNUTLS_MAJOR/gnutls-$GNUTLS_MINOR.tar.xz \  
&& LIBMICROHTTPD=0.9.51 \  
&& getpackage libmicrohttpd libtasn1.tar.gz
ftp://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-$LIBTASN1.tar.gz \  
&& GNURL=7_50_3 \  
&& wget \--no-check-certificate
https://gnunet.org/sites/default/files/gnurl-$GNURL.tar.bz2 -O gnurl.tar.bz2 \  
&& wget \--no-check-certificate
https://gnunet.org/sites/default/files/gnurl-$GNURL.tar.bz2.sig -O
gnurl.tar.bz2.sig \  
&& gpg \--verify gnurl.tar.bz2.sig gnurl.tar.bz2 \  
&& mkdir -p gnurl && cd gnurl \  
&& tar \--strip-components=1 -xf ../gnurl.tar.bz2 \  
&& ./configure \--enable-ipv6 \--with-gnutls \--without-libssh2 \--without-
libmetalink \--without-winidn \--without-librtmp \--without-nghttp2
\--without-nss \--without-cyassl \--without-polarssl \--without-ssl
\--without-winssl \--without-darwinssl \--disable-sspi \--disable-ntlm-wb
\--disable-ldap \--disable-rtsp \--disable-dict \--disable-telnet \--disable-
tftp \--disable-pop3 \--disable-imap \--disable-smtp \--disable-gopher
\--disable-file \--disable-ftp \  
&& make && make install \  
&& cd .. && rm -rf gnurl* \  
&& GNUNET_VERSION=0.10.1 \  
&& wget http://ftpmirror.gnu.org/gnunet/gnunet-$GNUNET_VERSION.tar.gz -O
gnunet.tar.gz \  
&& mkdir gnunet \  
&& cd gnunet \  
&& tar \--strip-components=1 -xf ../gnunet.tar.gz \  
&& ./configure \--includedir=/usr/local/include \--with-nssdir=/lib \--enable-
logging=verbose \  
&& adduser \--system \--home /var/lib/gnunet \--group \--disabled-password
gnunet \  
&& addgroup \--system gnunetdns \  
&& make && make install \  
# lastly  
&& apt-get purge -y \  
make \  
gcc \  
wget \  
libltdl-dev \  
libbluetooth-dev \  
libunbound-dev \  
libsqlite3-dev \  
libmysqlclient-dev \  
libp11-kit-dev \  
libgpg-error-dev \  
libunistring-dev \  
libidn11-dev \  
libglpk-dev \  
libextractor-dev \  
# libgstreamer1.0-dev \  
# libpulse-dev \  
# libopus-dev \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& ldconfig  
  
USER gnunet  
  
CMD gnunet-arm -s  

