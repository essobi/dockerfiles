# Copyright (c) 2017, rockyluke  
#  
# Permission to use, copy, modify, and/or distribute this software for any  
# purpose with or without fee is hereby granted, provided that the above  
# copyright notice and this permission notice appear in all copies.  
#  
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH  
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY  
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,  
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM  
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR  
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR  
# PERFORMANCE OF THIS SOFTWARE.  
  
FROM rockyluke/debian:jessie  
  
ENV DEBIAN_FRONTEND=noninteractive \  
VERSION=4.0.21 \  
ARCHIVE=v4/squid-4.0.21.tar.gz  
  
RUN apt-get update -qq && \  
apt-get upgrade -qq -y && \  
apt-get install -qq -y \  
autoconf \  
automake \  
build-essential \  
ed \  
libcap2-dev \  
libkrb5-dev \  
libltdl-dev \  
libsasl2-dev \  
libssl-dev \  
libtool \  
libtool-bin \  
squid-langpack \  
ssl-cert \  
wget && \  
apt-clean  
  
RUN curl -Ls -o /tmp/squid-${VERSION}.tar.gz \  
"http://www.squid-cache.org/Versions/${ARCHIVE}" && \  
tar -xzf /tmp/squid-${VERSION}.tar.gz -C /usr/src && \  
rm /tmp/squid-${VERSION}.tar.gz  
  
RUN cd /usr/src/squid-${VERSION} && \  
./bootstrap.sh && \  
./configure \  
\--prefix=/usr \  
\--libexecdir=${prefix}/lib/squid \  
\--sysconfdir=/etc/squid \  
\--localstatedir=/var \  
\--datadir=${prefix}/share/squid \  
\--disable-snmp \  
\--enable-http-violations \  
\--enable-follow-x-forwarded-for \  
\--enable-ssl \  
\--enable-ssl-crtd \  
\--disable-translation \  
\--with-logdir=/var/log/squid \  
\--with-pidfile=/var/run/squid.pid \  
\--with-default-user=proxy \  
\--with-openssl && \  
make all && \  
make install && \  
chown proxy:adm /var/log/squid && \  
rm -rf /usr/src/squid-${VERSION}  
  
RUN ln -s /lib/squid/security_file_certgen /bin/security_file_certgen && \  
/bin/security_file_certgen -c -s /var/lib/ssl_db && \  
chown -R proxy:proxy /var/lib/ssl_db  
  
EXPOSE 3128  
  
ENTRYPOINT [ "/usr/sbin/squid" ]  
  
CMD [ "-N" ]  
# EOF  

