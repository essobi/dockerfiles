FROM studionone/apache-php:7.1  
# Varnish is being installed from source because we need to VCL mod to allow
for dynamic configurations  
RUN apt-get update && apt-get install -y autoconf \  
automake \  
autotools-dev \  
libedit-dev \  
libjemalloc-dev \  
libncurses-dev \  
libpcre3-dev \  
libtool \  
pkg-config \  
python-docutils \  
python-sphinx \  
&& cd /tmp \  
&& wget https://github.com/varnishcache/varnish-
cache/archive/varnish-4.1.8.tar.gz \  
&& wget https://github.com/Dridi/libvmod-
querystring/releases/download/v1.0.1/vmod-querystring-1.0.1.tar.gz \  
&& tar xfz varnish-4.1.8.tar.gz \  
&& rm -rf /tmp/varnish-4.1.8.tar.gz \  
&& tar xfz vmod-querystring-1.0.1.tar.gz \  
&& rm -rf /tmp/vmod-querystring-1.0.1.tar.gz \  
&& cd /tmp/varnish-cache-varnish-4.1.8 \  
&& sh autogen.sh \  
&& sh configure \  
&& make && make install \  
# Varnish querystring module  
&& cd /tmp/vmod-querystring-1.0.1 \  
&& sh configure \  
&& make \  
&& make install \  
&& rm -rf /tmp/varnish-cache-varnish-4.1.8 \  
&& rm -rf /tmp/vmod-querystring-1.0.1 \  
&& ldconfig \  
&& mkdir -p /etc/varnish  
  
# Varnish defult configuration file  
COPY conf/default.vcl.m4 /opt/default.vcl.m4  
COPY conf/supervisor_conf.d/varnish.conf /etc/supervisor/conf.d/varnish.conf  
  

