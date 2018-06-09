FROM debian:jessie  
  
RUN \  
useradd -r -s /bin/false varnishd  
  
# Install Varnish source build dependencies.  
RUN \  
apt-get update && apt-get install -y --no-install-recommends \  
automake \  
build-essential \  
ca-certificates \  
curl \  
libedit-dev \  
libjemalloc-dev \  
libncurses-dev \  
libpcre3-dev \  
libtool \  
pkg-config \  
python-docutils \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Varnish from source, so that Varnish modules can be compiled and
installed.  
ENV VARNISH_VERSION=5.1.1  
ENV
VARNISH_SHA256SUM=6f4b85b52a827f28b3964fbe6a11296e2ed50156c70d511c10feff19459493ae  
RUN \  
apt-get update && \  
mkdir -p /usr/local/src && \  
cd /usr/local/src && \  
curl -sfLO https://repo.varnish-
cache.org/source/varnish-$VARNISH_VERSION.tar.gz && \  
echo "${VARNISH_SHA256SUM} varnish-$VARNISH_VERSION.tar.gz" | sha256sum -c -
&& \  
tar -xzf varnish-$VARNISH_VERSION.tar.gz && \  
cd varnish-$VARNISH_VERSION && \  
./autogen.sh && \  
./configure && \  
make install && \  
ldconfig && \  
rm ../varnish-$VARNISH_VERSION.tar.gz  
  
COPY start-varnishd.sh /usr/local/bin/start-varnishd  
  
ENV VARNISH_PORT 80  
ENV VARNISH_MEMORY 100m  
  
EXPOSE 80  
CMD ["start-varnishd"]  
  
ONBUILD COPY default.vcl /etc/varnish/default.vcl  

