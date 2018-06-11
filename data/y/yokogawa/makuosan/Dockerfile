FROM debian:stretch  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN set -ex \  
&& apt-get update \  
&& apt-get \--no-install-recommends -y install \  
curl \  
ca-certificates \  
gcc \  
make \  
libc-dev \  
libssl-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
# setup contents directory  
RUN set -ex \  
&& mkdir -p /var/www \  
&& chown www-data:www-data /var/www  
  
# install makuosan  
ENV MAKUOSAN_VERSION 1.3.6  
RUN set -ex \  
&& curl -sL
https://github.com/yasui0906/makuosan/archive/${MAKUOSAN_VERSION}.tar.gz | tar
xzf - \  
&& cd makuosan-${MAKUOSAN_VERSION} \  
&& ./configure \  
&& make \  
&& make install  
  
ENTRYPOINT ["makuosan"]  
CMD ["-b", "/var/www", "-u", "www-data", "-g", "www-data", "-n"]  

