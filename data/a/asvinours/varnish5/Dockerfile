FROM debian:stretch-slim  
  
LABEL maintainer "Fabrice Baumann"  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
curl \  
git \  
libvarnishapi-dev \  
libmhash-dev \  
autotools-dev \  
libtool \  
automake \  
make \  
pkg-config \  
python \  
python-docutils \  
dpkg-dev \  
autoconf \  
libncurses5-dev \  
xsltproc \  
groff-base \  
libpcre3-dev \  
r-recommended \  
libjemalloc-dev \  
tar  
  
ENV VARNISH_VERSION 5.1.1  
ENV VMOD_MODULES_VERSION 0.11.0  
RUN curl -SLO "https://github.com/varnishcache/varnish-
cache/archive/varnish-$VARNISH_VERSION.tar.gz" \  
&& mkdir -p /usr/local/varnish-cache \  
&& tar -xzvf "varnish-$VARNISH_VERSION.tar.gz" -C /usr/local/varnish-cache
--strip-components=1 \  
&& cd /usr/local/varnish-cache \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
RUN curl -SLO "https://github.com/varnish/varnish-
modules/archive/$VMOD_MODULES_VERSION.tar.gz" \  
&& mkdir -p /usr/local/varnish-modules \  
&& tar -xzvf "$VMOD_MODULES_VERSION.tar.gz" -C /usr/local/varnish-modules
--strip-components=1 \  
&& cd /usr/local/varnish-modules \  
&& ./bootstrap \  
&& ./configure VARNISHSRC=/usr/src/varnish-cache/ \  
&& make \  
&& make install  
  
ENV PKG_CONFIG_PATH "/usr/src/varnish-cache/lib/pkgconfig"  
RUN curl -SLO "https://github.com/varnish/libvmod-digest/archive/libvmod-
digest-1.0.1.tar.gz" \  
&& mkdir -p /usr/local/varnish-digest \  
&& tar -xzvf "libvmod-digest-1.0.1.tar.gz" -C /usr/local/varnish-digest
--strip-components=1 \  
&& cd /usr/local/varnish-digest \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
RUN ldconfig # rebuild the library cache (otherwise varnishlog will cry)  
COPY start.sh /start.sh  
  
EXPOSE 80  
EXPOSE 6082  
CMD ["/start.sh"]  
  

