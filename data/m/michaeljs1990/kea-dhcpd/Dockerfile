FROM ubuntu:xenial as builder  
  
RUN apt-get update \  
&& apt-get install -y dh-autoreconf \  
libssl-dev liblog4cplus-dev libboost-dev \  
libboost-system-dev libmysqlclient-dev git \  
xsltproc elinks xorg-docs xmlto  
  
RUN git clone https://github.com/isc-projects/kea.git  
  
WORKDIR /kea  
  
RUN autoreconf --install \  
&& ./configure --prefix=/usr \  
\--sbindir=/usr/bin \  
\--libexecdir=/usr/bin \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--with-dhcp-mysql \  
\--enable-generate-docs \  
&& make -j4 DESTDIR=/kea install  
  
FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get install -y libssl1.0.0 \  
libmysqlclient20 liblog4cplus-1.1-9 \  
libboost-system1.58.0 man \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /etc/kea \  
&& mkdir -p /var/kea \  
&& mkdir -p /var/run/kea  
  
# Example config files only good for reference  
COPY kea-ca.conf /etc/kea  
COPY kea.conf /etc/kea  
COPY keactrl.conf /etc/kea  
  
# Install shared objects and binaries  
COPY \--from=builder /kea/usr/lib/ /usr/lib  
COPY \--from=builder /kea/usr/share/kea/ /usr/share/kea  
COPY \--from=builder /kea/usr/bin/ /usr/bin  
  
# Configure those sweet sweet man pages  
RUN mkdir -p /usr/local/share/man/man8/  
COPY \--from=builder /kea/usr/share/man/man8/ /usr/local/share/man/man8  
RUN mandb  

