FROM debian:latest  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
RUN apt-get update \  
&& apt-get --no-install-recommends -y install \  
curl \  
gcc \  
make \  
automake \  
libc6-dev \  
libssl-dev \  
libevent-dev \  
libexpat1-dev \  
ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ARG UNBOUND_VERSION=1.5.6  
RUN curl -LO
https://www.unbound.net/downloads/unbound-${UNBOUND_VERSION}.tar.gz \  
&& tar xzf unbound-${UNBOUND_VERSION}.tar.gz \  
&& cd unbound-${UNBOUND_VERSION} \  
&& ./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--with-libevent=/usr \  
\--with-run-dir=/var/unbound \  
&& make -j $(nproc) \  
&& make install \  
&& rm -rf /unbound-${UNBOUND_VERSION} /unbound-${UNBOUND_VERSION}.tar.gz  
  
RUN useradd -s /bin/false -m -d /var/lib/unbound unbound  
COPY unbound.conf /etc/unbound/unbound.conf  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["unbound"]  

