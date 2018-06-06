FROM alpine:latest  
  
# Define build argument for version  
ARG VERSION  
  
RUN set -x && \  
\  
# Install build tools, libraries and utilities \  
apk add --no-cache --virtual .build-deps \  
build-base \  
gnupg \  
pcre-dev \  
wget \  
zlib-dev && \  
\  
# Retrieve, verify and unpack Nginx source \  
TMP="$(mktemp -d)" && cd "$TMP" && \  
gpg --keyserver pgp.mit.edu --recv-keys \  
B0F4253373F8F6F510D42178520A9993A1C052F8 && \  
wget -q http://nginx.org/download/nginx-${VERSION}.tar.gz && \  
wget -q http://nginx.org/download/nginx-${VERSION}.tar.gz.asc && \  
gpg --verify nginx-${VERSION}.tar.gz.asc && \  
tar -xf nginx-${VERSION}.tar.gz && \  
\  
# Build and install nginx \  
cd nginx-${VERSION} && \  
./configure \  
\--with-ld-opt="-static" \  
\--with-http_sub_module && \  
make install && \  
strip /usr/local/nginx/sbin/nginx && \  
\  
# Clean up \  
cd / && rm -rf "$TMP" && \  
apk del .build-deps && \  
\  
# Symlink access and error logs to /dev/stdout and /dev/stderr, \  
# in order to make use of Docker's logging mechanism \  
ln -sf /dev/stdout /usr/local/nginx/logs/access.log && \  
ln -sf /dev/stderr /usr/local/nginx/logs/error.log  
  
# Customise static content, and configuration  
COPY index.html /usr/local/nginx/html/  
COPY nginx.conf /usr/local/nginx/conf/  
  
# Add entrypoint script  
COPY docker-entrypoint.sh /  
  
# Change default stop signal from SIGTERM to SIGQUIT  
STOPSIGNAL SIGQUIT  
  
# Expose port  
EXPOSE 80  
# Define entrypoint and default parameters  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]  

