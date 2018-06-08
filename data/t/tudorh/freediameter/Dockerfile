FROM alpine  
MAINTAINER Tudor Holton <development@tudorholton.com>  
RUN apk update \  
&& apk add build-base cmake wget tar gzip file linux-headers bison flex glib
libgcrypt glib-dev libidn-dev gnutls-dev libgcrypt-dev gnutls libidn gnutls-
utils ca-certificates \  
&& wget -O libsctp.tar.gz
http://downloads.sourceforge.net/project/lksctp/lksctp-tools/lksctp-
tools-1.0.17.tar.gz \  
&& mkdir build-libsctp \  
&& cd build-libsctp \  
&& tar xzvf ../libsctp.tar.gz \--strip-components=1 \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install \  
&& cd - \  
&& rm -R libsctp.tar.gz build-libsctp \  
&& wget -O freediameter.tar.gz
http://www.freediameter.net/hg/freeDiameter/archive/1.2.0.tar.gz \  
&& mkdir build-freediameter \  
&& cd build-freediameter \  
&& tar xzvf ../freediameter.tar.gz \--strip-components=1 \  
&& cmake -DCMAKE_INSTALL_PREFIX=/usr -DDEFAULT_CONF_PATH=/etc/freeDiameter
-DBUILD_TESTING:BOOL=OFF -Wno-dev .\  
&& make \  
&& make install \  
&& mkdir -p /etc/freeDiameter \  
&& cp doc/freediameter.conf.sample /etc/freeDiameter/freeDiameter.conf.sample
\  
&& cd - \  
&& rm -R freediameter.tar.gz build-freediameter \  
&& apk del build-base cmake wget tar gzip linux-headers glib-dev bison flex
libgcrypt-dev libidn-dev gnutls-dev  
ADD ["rootcert.template", "diametercert.template", "/etc/ssl/"]  
ADD ["startup.sh", "/"]  
EXPOSE 3868 5658  
CMD ["/startup.sh"]  

