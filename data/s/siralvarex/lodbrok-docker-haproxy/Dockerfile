FROM ubuntu-debootstrap:14.04  
RUN apt-get update && apt-get install -y libssl1.0.0 libpcre3 \--no-install-
recommends && rm -rf /var/lib/apt/lists/*  
  
ENV HAPROXY_MAJOR 1.5  
ENV HAPROXY_VERSION 1.5.14  
ENV HAPROXY_MD5 ad9d7262b96ba85a0f8c6acc6cb9edde  
  
# see http://sources.debian.net/src/haproxy/1.5.8-1/debian/rules/ for some
helpful navigation of the possible "make" arguments  
RUN buildDeps='curl gcc libc6-dev libpcre3-dev libssl-dev make' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& curl -SL
"http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz"
-o haproxy.tar.gz \  
&& echo "${HAPROXY_MD5} haproxy.tar.gz" | md5sum -c \  
&& mkdir -p /usr/src/haproxy \  
&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy \--strip-components=1 \  
&& rm haproxy.tar.gz \  
&& make -C /usr/src/haproxy \  
TARGET=linux2628 \  
USE_PCRE=1 PCREDIR= \  
USE_OPENSSL=1 \  
USE_ZLIB=1 \  
all \  
install-bin \  
&& mkdir -p /usr/local/etc/haproxy \  
&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \  
&& rm -rf /usr/src/haproxy \  
&& apt-get purge -y \--auto-remove $buildDeps  
  
RUN apt-get update && apt-get install -y openssl iptables \  
&& openssl genrsa -out _.marathon.mesos.key 2048 \  
&& openssl req -new -x509 -key _.marathon.mesos.key -out _.marathon.mesos.cert
-days 3650 -subj /CN=\\*.marathon.mesos \  
&& cat _.marathon.mesos.key > /haproxy.pem \  
&& cat _.marathon.mesos.cert >> /haproxy.pem && rm -f *marathon.mesos.* \  
&& apt-get purge -y \--auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash", "-c", "while true; do ps aux | grep haproxy; sleep 60;
done"]  

