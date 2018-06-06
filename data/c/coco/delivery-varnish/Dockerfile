FROM alpine:3.4  
  
ENV VARNISHSRC=/usr/include/varnish VMODDIR=/usr/lib/varnish/vmods  
  
RUN apk --update add varnish varnish-dev git automake autoconf libtool python
make py-docutils curl jq && \  
git clone https://github.com/varnish/libvmod-vsthrottle.git && \  
cd libvmod-vsthrottle && \  
git checkout 9fc90ebdd56a75a149583d70ec732b99fe0b48e9 && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
cd / && echo "-------basicauth-build-------" && \  
git clone http://git.gnu.org.ua/repo/vmod-basicauth.git && \  
cd vmod-basicauth && \  
git clone http://git.gnu.org.ua/repo/acvmod.git && \  
git checkout 2a76106cbd56643757ab8096c4674bb55253a1ed && \  
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
  
COPY default.vcl /etc/varnish/default.vcl  
COPY start.sh /start.sh  
  
RUN chmod +x /start.sh  
  
EXPOSE 80  
CMD ["/start.sh"]  

