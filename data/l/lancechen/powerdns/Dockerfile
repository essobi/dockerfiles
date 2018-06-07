FROM alpine:3.3  
MAINTAINER Lance Chen <cyen0312@gmail.com>  
  
ENV PDNS_VERSION 3.4.8  
RUN apk update \  
&& apk add curl build-base boost-dev \  
&& rm -rf /var/cache/apk/*  
  
ADD pdns.conf /etc/pdns.conf  
ADD 0001-Add-a-disable-syslog-setting.patch /tmp/0001-Add-a-disable-syslog-
setting.patch  
ADD force-libgcc_s-preload-on-glibc-only.patch /tmp/force-libgcc_s-preload-on-
glibc-only.patch  
  
RUN curl -O -L
"https://downloads.powerdns.com/releases/pdns-${PDNS_VERSION}.tar.bz2" \  
&& tar xjf "pdns-${PDNS_VERSION}.tar.bz2" \  
&& cd "pdns-${PDNS_VERSION}" \  
&& patch -p1 < /tmp/0001-Add-a-disable-syslog-setting.patch \  
&& patch -p1 < /tmp/force-libgcc_s-preload-on-glibc-only.patch \  
&& ./configure --prefix=/usr \  
\--sysconfdir=/etc \  
\--mandir=/usr/share/man \  
\--infodir=/usr/share/info \  
\--localstatedir=/var \  
\--libdir=/usr/lib \  
\--with-modules="" \  
\--with-dynmodules="bind geo" \  
\--disable-static \  
&& make \  
&& make install  
  
CMD ["pdns_server"]  

