# Build with official ubuntu image  
FROM ubuntu:14.04  
  
# Expose ports for http and ssl requests  
EXPOSE 80  
EXPOSE 443  
  
# http://nginx.org/en/download.html  
ENV NGINX_VERSION 1.11.4  
  
# https://github.com/pagespeed/ngx_pagespeed/releases  
ENV PAGESPEED_VERSION 1.11.33.4  
  
# https://www.openssl.org/source  
ENV OPENSSL_VERSION 1.0.2i  
  
# Create new nginx user  
RUN useradd -r -s /usr/sbin/nologin nginx && mkdir -p /var/log/nginx
/var/cache/nginx  
# Update the system  
RUN apt-get update  
# Install external dependencys with apt-get  
RUN apt-get -y --no-install-recommends install git-core autoconf automake
libtool build-essential zlib1g-dev libpcre3-dev libxslt1-dev libxml2-dev
libgd2-xpm-dev libgeoip-dev libgoogle-perftools-dev libperl-dev  
  
###############################################################################  
# Get the intall packages from the local machine #  
###############################################################################  
# Adds and extracts the nginx version to the /tmp folder  
#ADD ./nginx-${NGINX_VERSION}.tar.gz /tmp  
# Adds and extracts the nginx verion of pagespeed to the /tmp folder  
#ADD ngx_pagespeed-${PAGESPEED_VERSION}-beta.tar /tmp  
# Adds and extracts psol to the /tmp/pagespeed folder so dont change the
download and extracton order  
#ADD ${PAGESPEED_VERSION}.tar /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta  
# Adds and extracs the openSSL version to the /tmp folder  
#ADD openssl-${OPENSSL_VERSION}.tar /tmp  
  
###############################################################################  
# Get the install packages from the git repositories #  
###############################################################################  
# Download the nginx version  
ADD http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz nginx.tar.gz  
# Extract and remove the nginx package to the /tmp folder  
RUN tar zxf nginx.tar.gz -C /tmp && rm -f nginx.tar.gz  
# Download the nginx version  
ADD
https://github.com/pagespeed/ngx_pagespeed/archive/v${PAGESPEED_VERSION}-beta.tar.gz
pagespeed.tar.gz  
# Extract and remove the ngx_pagespeed package to the /tmp folder  
RUN tar zxf pagespeed.tar.gz -C /tmp && rm -f pagespeed.tar.gz  
# Download the psol version  
ADD https://dl.google.com/dl/page-speed/psol/${PAGESPEED_VERSION}.tar.gz
psol.tar.gz  
# Extract and remove the psol package to the /tmp/pagespeed-version dolder so
do not change the download/extraction order  
RUN tar xzf psol.tar.gz -C /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta && rm
-f psol.tar.gz  
# Download the openSSL version  
ADD https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz
openssl.tar.gz  
# Extract and remove the openssl package to the /tmp folder  
RUN tar xzf openssl.tar.gz -C /tmp && rm -f openssl.tar.gz  
  
# Create the nginx config fiele to initialize the modules  
RUN cd /tmp/nginx-${NGINX_VERSION} && \  
./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--user=nginx \  
\--group=nginx \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_stub_status_module \  
\--with-http_auth_request_module \  
\--without-http_autoindex_module \  
\--without-http_ssi_module \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-file-aio \  
\--with-http_v2_module \  
\--with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat
-Werror=format-security -Wp,-D_FORTIFY_SOURCE=2' \  
\--with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,--as-needed' \  
\--with-ipv6 \  
\--with-pcre-jit \  
\--with-openssl=/tmp/openssl-${OPENSSL_VERSION} \  
\--add-module=/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta && \  
make && \  
make install && \  
apt-get purge -yqq automake autoconf libtool git-core build-essential
zlib1g-dev libpcre3-dev libxslt1-dev libxml2-dev libgd2-xpm-dev libgeoip-dev
libgoogle-perftools-dev libperl-dev && \  
apt-get autoremove -yqq && \  
apt-get clean && \  
rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
# Copy all image files to the docker container  
COPY . /app  
# Set permissions for the init file  
RUN chmod 750 ./app/bin/init_nginx.sh  
# Run the init file  
RUN ./app/bin/init_nginx.sh  
# Start the nginx with default startup entrypoint  
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]  

