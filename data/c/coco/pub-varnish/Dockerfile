FROM alpine  
  
ENV VARNISHSRC=/usr/include/varnish VMODDIR=/usr/lib/varnish/vmods  
ADD fmt /usr/bin/fmt  
  
RUN apk --update add varnish varnish-dev git automake autoconf libtool python
make py-docutils && \  
git clone https://github.com/varnish/libvmod-vsthrottle.git && \  
cd libvmod-vsthrottle && \  
git checkout 9fc90ebdd56a75a149583d70ec732b99fe0b48e9 && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
cd / && \  
chmod +x /usr/bin/fmt && \  
git clone http://git.gnu.org.ua/repo/vmod-basicauth.git && \  
cd vmod-basicauth && \  
git checkout cb7aa1e857db51e2b0e31c66427f9107cf6d3a5c && \  
mkdir -p /usr/include/varnish/bin/varnishtest/ && \  
ln -s /usr/bin/varnishtest /usr/include/varnish/bin/varnishtest/varnishtest &&
\  
mkdir -p /usr/include/varnish/lib/libvcc/ && \  
ln -s /usr/share/varnish/vmodtool.py
/usr/include/varnish/lib/libvcc/vmodtool.py && \  
./bootstrap && \  
./configure && \  
make && \  
make install && \  
apk del git automake autoconf libtool python make py-docutils && \  
rm -rf /var/cache/apk/* /libvmod-vsthrottle /vmod-basicauth  
  
ADD default.vcl /etc/varnish/default.vcl  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
EXPOSE 80  
CMD ["/start.sh"]  

