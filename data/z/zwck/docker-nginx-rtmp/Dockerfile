FROM gliderlabs/alpine:latest  
ENV RTMPID 1101  
  
# Create nginx user  
RUN addgroup -g ${RTMPID} nginx && \  
adduser -G nginx -u ${RTMPID} -S nginx  
  
# Build tini and nginx-rtmp from source  
RUN apk update \  
&& apk add build-base cmake git pcre-dev openssl-dev \  
&& mkdir -p /opt/src /opt/rtmp \  
&& cd /opt/src \  
&& git clone https://github.com/krallin/tini \  
&& git clone git://github.com/arut/nginx-rtmp-module.git \  
&& git clone https://github.com/nginx/nginx.git \  
&& cd /opt/src/tini \  
&& cmake . && make && make install \  
&& cp tini / \  
&& cd /opt/src/nginx \  
&& auto/configure --prefix=/opt/nginx \  
\--user=nginx --group=nginx \  
\--with-http_ssl_module \  
\--with-http_secure_link_module \  
\--add-module=/opt/src/nginx-rtmp-module \  
\--http-client-body-temp-path=/opt/rtmp/client_body \  
\--http-proxy-temp-path=/opt/rtmp/proxy \  
\--http-fastcgi-temp-path=/opt/rtmp/fastcgi \  
\--http-uwsgi-temp-path=/opt/rtmp/uwsgi \  
\--http-scgi-temp-path=/opt/rtmp/scgi \  
&& make \  
&& make install \  
&& mkdir /opt/nginx/rtmp-module \  
&& cp /opt/src/nginx-rtmp-module/stat.xsl /opt/nginx/rtmp-module/ \  
&& apk del build-base cmake git pcre-dev openssl-dev \  
&& apk add pcre openssl \  
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/* /opt/src \  
&& chown -R nginx:nginx /opt/nginx /opt/rtmp  
  
# Install static ffmpeg build lets hope its ffmpeg 4.0  
RUN cd /opt \  
&& wget -q -O- "https://johnvansickle.com/ffmpeg/releases/ffmpeg-
release-64bit-static.tar.xz" | tar -xJv \  
&& mv ffmpeg*/* /usr/local/bin \  
&& rm -rf /opt/ffmpeg*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /opt/nginx/logs/access.log \  
&& ln -sf /dev/stderr /opt/nginx/logs/error.log  
  
# Recordings, bodies and other config files to be stored here  
# Do not forget to chown this volume to uid 1000 : gid 1000!!!  
VOLUME /opt/rtmp  
  
# Default config file. Listens at port 8000 and loads  
# anything under /opt/nginx/conf.d  
ADD nginx.conf /opt/nginx/conf/nginx.conf  
  
EXPOSE 8080 1935  
  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
CMD [ "opt/nginx/sbin/nginx" ]  

