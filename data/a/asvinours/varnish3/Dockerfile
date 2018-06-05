FROM debian:stretch-slim  
  
# References  
# https://www.varnish-
cache.org/docs/3.0/installation/install.html#configuring-and-compiling  
# http://blog.tenya.me/blog/2013/10/25/geoip-with-varnish/  
  
RUN apt-get update && apt-get install -y \  
python \  
python-docutils \  
libmhash-dev \  
dpkg-dev \  
autotools-dev \  
automake1.11 \  
libtool \  
autoconf \  
libncurses5-dev \  
xsltproc \  
groff-base \  
libpcre3-dev \  
pkg-config \  
r-recommended \  
libjemalloc-dev \  
tar  
  
COPY libvmod.tar.gz /usr/src/libvmod.tar.gz  
  
# Compile varnish  
RUN cd /usr/src \  
&& tar -xvf libvmod.tar.gz \  
&& cd varnish-cache \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
# Compile vmods  
RUN cd /usr/src \  
&& for vmodDir in libvmod-digest libvmod-header libvmod-timeutils libvmod-var;
do \  
cd /usr/src/$vmodDir \  
&& ./autogen.sh \  
&& ./configure VARNISHSRC=/usr/src/varnish-cache/ \  
&& make \  
&& make install; \  
done  
  
RUN ldconfig # rebuild the library cache (otherwise varnishlog will cry)  
  
COPY start.sh /start.sh  
  
EXPOSE 80  
EXPOSE 6082  
  
CMD ["/start.sh"]  

