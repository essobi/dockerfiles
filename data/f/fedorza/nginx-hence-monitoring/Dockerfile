FROM ubuntu:16.04  
MAINTAINER Fedor Zakharov<fedor@therefore.ca>  
  
  
  
ENV HENCE_PREFIX=/opt/hence \  
HENCE_USER=hence \  
HENCE_APP_NAME=nginx \  
HENCE_APP_USER=hence \  
HENCE_APP_VERSION=4.0.0  
ENV HENCE_APP_DIR=$HENCE_PREFIX/$HENCE_APP_NAME \  
HENCE_APP_VOL_PREFIX=/hence/$HENCE_APP_NAME  
ENV PATH=$HENCE_APP_DIR/sbin:$HENCE_PREFIX/common/bin:$PATH  
  
COPY help.txt $HENCE_PREFIX/help.txt  
COPY post-install.sh /tmp/post-install.sh  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.13.0.0/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
RUN apt update && apt upgrade -y  
RUN apt install sudo  
RUN echo $HENCE_USER  
RUN printf '#!/bin/bash\n. $HENCE_PREFIX/hence-
utils.sh\nprint_hence_help_page' > '/usr/bin/print-help' && \  
printf '#!/bin/bash\n. $HENCE_PREFIX/hence-utils.sh\ncheck_for_updates' >
'/usr/bin/check-updates' && \  
chmod a+x /usr/bin/print-help /usr/bin/check-updates && \  
adduser $HENCE_USER && \  
sed -i -e 's/\s*Defaults\s*secure_path\s*=/# Defaults secure_path=/'
/etc/sudoers && \  
echo "hence ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
COPY install.sh $HENCE_PREFIX/install.sh  
COPY hence-utils.sh $HENCE_PREFIX/hence-utils.sh  
  
RUN apt install build-essential wget git gettext -y  
  
RUN wget https://nginx.org/download/nginx-1.13.6.tar.gz && tar zxvf
nginx-1.13.6.tar.gz  
RUN wget https://ftp.pcre.org/pub/pcre/pcre-8.40.tar.gz && tar xzvf
pcre-8.40.tar.gz  
RUN wget http://www.zlib.net/zlib-1.2.11.tar.gz && tar xzvf zlib-1.2.11.tar.gz  
RUN wget https://www.openssl.org/source/openssl-1.1.0f.tar.gz && tar xzvf
openssl-1.1.0f.tar.gz  
RUN git clone git://github.com/vozlt/nginx-module-vts.git  
RUN rm -rf *.tar.gz  
RUN mkdir /var/lib/nginx  
RUN mkdir /var/lib/nginx/client_body  
RUN cd nginx-1.13.6 && ./configure --prefix=/usr/share/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/run/nginx.pid \  
\--lock-path=/var/lock/nginx.lock \  
\--user=www-data \  
\--group=www-data \  
\--build=Ubuntu \  
\--add-module=../nginx-module-vts \  
\--http-client-body-temp-path=/var/lib/nginx/client_body \  
\--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \  
\--http-proxy-temp-path=/var/lib/nginx/proxy \  
\--http-scgi-temp-path=/var/lib/nginx/scgi \  
\--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \  
\--with-pcre=../pcre-8.40 \  
\--with-pcre-jit \  
\--with-zlib=../zlib-1.2.11 \  
\--with-compat \  
\--with-file-aio \  
\--with-threads \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_slice_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_secure_link_module \  
\--with-mail \  
\--with-stream \  
\--with-debug && make && make install  
  
COPY rootfs /  
  
RUN sh $HENCE_PREFIX/install.sh && \  
s6-rmrf /etc/s6/services/s6-fdholderd/down  
  
EXPOSE 80 88 443  
VOLUME ["/etc/nginx/custom.d", "/app", "$HENCE_APP_VOL_PREFIX/conf",
"$HENCE_APP_VOL_PREFIX/logs/nginx-access-logs",
"$HENCE_APP_VOL_PREFIX/logs/nginx-error-logs"]  
  
WORKDIR /app  
  
ENTRYPOINT ["/init"]  
  
CMD []  

