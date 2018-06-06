# Pull base image.  
FROM debian:jessie  
  
# Set the working directory so forego sees the Procfile  
WORKDIR /opt/openresty  
  
# Expose volume for SSL certificates  
VOLUME ["/etc/nginx/certs"]  
  
# Expose volume for externally linked configurations  
VOLUME ["/etc/nginx/external-conf.d"]  
  
# Install packages.  
RUN \  
apt-get -qq update \  
&& apt-get install -yq build-essential \  
curl \  
libreadline-dev \  
libncurses5-dev \  
libpcre3-dev \  
libssl-dev \  
lua5.2 \  
luarocks \  
nano \  
perl \  
wget  
  
RUN \  
curl -sSL "$(curl https://dl.equinox.io/ddollar/forego/stable | grep -Po
'(?<=href=")[^"]*' | grep 'forego-stable-linux-amd64.tgz')" \  
| tar xz -C /usr/local/bin \  
&& chmod u+x /usr/local/bin/forego  
  
ENV OPENRESTY_VER 1.11.2.1  
ENV DOCKER_GEN_VERSION 0.7.3  
ENV NGX_SUBSTITUTIONS_FILTER_VERSION 0.6.4  
  
RUN \  
curl -L "https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz" \  
| tar -C /usr/local/bin -xvzf - \  
&& curl -L "https://openresty.org/download/openresty-$OPENRESTY_VER.tar.gz" \  
| tar -xzvf - && \  
cd openresty-$OPENRESTY_VER && \  
curl -sSL
"https://github.com/yaoweibin/ngx_http_substitutions_filter_module/archive/v$NGX_SUBSTITUTIONS_FILTER_VERSION.tar.gz"
\  
| tar xz && \  
./configure --with-pcre-jit --with-ipv6 --add-
module=./ngx_http_substitutions_filter_module-$NGX_SUBSTITUTIONS_FILTER_VERSION
&& \  
make && \  
make install && \  
make clean && \  
cd .. && \  
rm -rf openresty-$OPENRESTY_VER && \  
ln -s /usr/local/openresty/nginx/sbin/nginx /usr/local/bin/nginx && \  
ldconfig && \  
mkdir -p /etc/nginx/conf.d  
  
# Add files to the container.  
COPY Procfile /opt/openresty/  
COPY nginx.tmpl /opt/openresty/  
COPY default.conf /etc/nginx/nginx.conf  
  
CMD ["forego","start","-r"]  

