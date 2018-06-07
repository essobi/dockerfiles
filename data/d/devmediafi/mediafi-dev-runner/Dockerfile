FROM node:0.10.35  
  
ENV VERSION='v0.0.5'  
  
WORKDIR /root  
  
RUN apt-get -y update \  
&& apt-get -y install ca-certificates libpcre3 libpcre3-dev rsync  
  
RUN curl -SL -o /usr/local/bin/forego
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego \  
&& chmod +x /usr/local/bin/forego \  
&& adduser \--disabled-password \--gecos '' nginx \  
&& curl -SLO http://nginx.org/download/nginx-1.7.10.tar.gz \  
&& tar -xvf nginx-1.7.10.tar.gz \  
&& rm nginx-1.7.10.tar.gz \  
&& cd nginx-1.7.10 \  
&& ./configure \--prefix=/usr \--conf-path=/etc/nginx/nginx.conf \--user=nginx
\--group=nginx \--with-poll_module \--without-select_module \--with-
http_ssl_module \--with-http_spdy_module \--with-http_gzip_static_module
\--with-http_auth_request_module \--with-pcre \--with-pcre-jit \  
&& make \  
&& make install \  
&& mkdir -p /usr/share/nginx/html \  
&& mkdir /var/log/nginx \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& rm -rf nginx-1.7.10  
  
RUN curl -SL "https://github.com/fic2/fic2-dev-
runner/releases/download/${VERSION}/fic2-dev-runner_${VERSION}.tar.gz" | tar
-zx -C /usr/share/nginx/html \--wildcards 'fic2-dev-runner_v*/dist' \--strip 2  
  
RUN mkdir /tmp/src && \  
curl -SL "https://github.com/fic2/fic2-dev-runner/archive/${VERSION}.tar.gz" |
tar -zx -C /tmp/src \--strip 1 \  
&& rsync -vah /tmp/src/prod/ /etc/ \  
&& mv /tmp/src/idm/* /root/ \  
&& npm install \  
&& rm -rf /tmp/src \  
&& unlink config.json \  
&& ln -s /usr/share/nginx/html/config.json  
  
RUN find /usr/share/nginx/html -type f -exec /bin/bash -c "/bin/gzip --verbose
-9 -c '{}' > '{}'.gz" \;  
  
EXPOSE 80 443  
  
CMD ["/usr/local/bin/forego", "start", "-f", "/etc/Procfile"]

