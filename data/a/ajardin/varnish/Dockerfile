FROM debian:jessie  
  
MAINTAINER Alexandre Jardin <info@ajardin.fr>  
LABEL maintainer="Alexandre Jardin <info@ajardin.fr>"  
  
# Install Varnish 4.0 with dependencies  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
automake \  
autotools-dev \  
ca-certificates \  
git \  
libtool \  
libvarnishapi-dev \  
make \  
pkg-config \  
python-docutils \  
varnish=4.0.2-1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Configure Varnish and libvmod-header  
RUN \  
git clone https://github.com/varnish/libvmod-header.git /tmp/libvmod-header &&
\  
cd /tmp/libvmod-header && git checkout 4.0 && \  
./autogen.sh && ./configure && make install && \  
rm -rf /tmp/libvmod-header  
  
# Install custom entrypoint  
COPY ./entrypoint.sh /usr/local/bin/docker-custom-entrypoint  
RUN chmod 777 /usr/local/bin/docker-custom-entrypoint  
ENTRYPOINT ["docker-custom-entrypoint"]  

