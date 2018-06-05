# Starting from Ubuntu and not from alpine, as libvmod-dynamic used for
generating dynamic backends  
# compiles currently only on debian based images.  
FROM ubuntu:trusty  
  
ENV VARNISHSRC=/usr/include/varnish VMODDIR=/usr/lib/varnish/vmods  
  
RUN apt-get update -q && \  
apt-get install -qq git curl apt-transport-https autotools-dev automake
autoconf libtool python make python-docutils && \  
curl -L https://packagecloud.io/varnishcache/varnish41/gpgkey | sudo apt-key
add \- && \  
echo "deb https://packagecloud.io/varnishcache/varnish41/ubuntu/ trusty main"
| tee /etc/apt/sources.list.d/varnish-cache.list && \  
apt-get -q update && \  
apt-get install -qq varnish varnish-dev && \  
cd / && echo "-------mod-dynamic build -------" && \  
git clone -b 4.1 https://github.com/nigoroll/libvmod-dynamic.git && \  
cd libvmod-dynamic && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
apt-get remove -qq git curl apt-transport-https autotools-dev automake
autoconf libtool python make python-docutils --force-yes && \  
apt-get -qq autoremove && \  
apt-get -qq clean && \  
rm -rf /libvmod-dynamic  
  
COPY default.vcl /etc/varnish/default.vcl  
COPY start.sh /start.sh  
  
RUN chmod +x /start.sh  
EXPOSE 80  
CMD ["/start.sh"]  

