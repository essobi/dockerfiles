FROM bitnami/minideb:jessie  
  
MAINTAINER Raymond Walker  
  
COPY sources.list /etc/apt/sources.list  
  
ENV SIEGE_VERSION="4.0.4" \  
DEBIAN_FRONTEND="noninteractive"  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -qy \  
wget \  
g++ \  
make \  
libssl-dev \  
zlib1g \  
&& wget --retry-connrefused --waitretry=1 -t 5 \--progress=bar -O -
"http://download.joedog.org/siege/siege-${SIEGE_VERSION}.tar.gz" | tar xzf -
-C /tmp \  
&& cd /tmp/siege-${SIEGE_VERSION} \  
&& ./configure \  
&& make install \  
&& apt-get -qy purge g++ make libssl-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& cd / \  
&& rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/* \  
rm -fr /usr/share/man/* /usr/share/doc/* /usr/share/locale/*  
  
# Raise the limits to successfully run benchmarks  
RUN ulimit -c -m -s -t unlimited  
  
ENTRYPOINT ["siege"]  
CMD ["--help"]  

