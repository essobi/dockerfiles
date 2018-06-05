FROM ubuntu:16.04  
#  
RUN mkdir /nginx  
  
#  
WORKDIR /nginx  
  
RUN set -x && \  
apt-get update && \  
apt-get install --no-install-recommends --no-install-suggests -y \  
wget git lbzip2 build-essential libssl-dev ca-certificates \  
  
&& wget http://nginx.org/download/nginx-1.12.2.tar.gz && \  
tar xvf nginx-1.12.2.tar.gz \  
  
&& wget
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.38.tar.bz2 && \  
tar xvf pcre-8.38.tar.bz2 \  
  
&& wget https://fossies.org/linux/misc/zlib-1.2.11.tar.gz && \  
tar xvf zlib-1.2.11.tar.gz \  
  
&& git clone https://github.com/orange-jacky/nginx-gridfs.git && \  
cd nginx-gridfs && \  
git submodule init && \  
git submodule update \  
  
&& cd .. \  
&& cd nginx-1.12.2/ && \  
./configure --prefix=/nginx \  
\--with-cc-opt="-static -static-libgcc" \--with-ld-opt="-static" \  
\--with-pcre=../pcre-8.38 \--with-zlib=../zlib-1.2.11 \  
\--with-http_ssl_module \  
\--add-module=../nginx-gridfs \  
&& make \  
&& make install \  
  
&& apt-get remove -y wget git lbzip2 build-essential libssl-dev ca-
certificates \  
&& cd .. \  
&& rm -rf zlib-1.2.11* nginx-gridfs pcre-8.38* nginx-1.12.2* \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
#  
EXPOSE 80 443  
#  
VOLUME /nginx /nginx/conf /nginx/logs /nginx/html  
CMD /nginx/sbin/nginx -c /nginx/conf/nginx.conf -g 'daemon off;'  

