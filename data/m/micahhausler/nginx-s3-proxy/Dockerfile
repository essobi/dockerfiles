FROM debian:jessie  
  
WORKDIR /tmp  
  
ENV NGINX_VERSION 1.11.1  
RUN apt-get -y update \  
&& apt-get -y install \  
curl \  
build-essential \  
libpcre3 \  
libpcre3-dev \  
zlib1g-dev \  
libssl-dev \  
wget \  
git \  
&& curl -LO http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz \  
&& tar zxf nginx-$NGINX_VERSION.tar.gz \  
&& cd nginx-$NGINX_VERSION \  
&& git clone -b AuthV2 https://github.com/anomalizer/ngx_aws_auth.git \  
&& ./configure --with-http_ssl_module --add-module=ngx_aws_auth \  
&& make install \  
&& cd /tmp \  
&& rm -f nginx-$NGINX_VERSION.tar.gz \  
&& rm -rf nginx-$NGINX_VERSION \  
&& apt-get purge -y curl git \  
&& apt-get autoremove -y  
  
RUN mkdir -p /data/cache  
RUN mkdir -p /etc/nginx/ssl /etc/nginx/sites-enabled \  
&& cp /usr/local/nginx/conf/mime.types /etc/nginx/mime.types  
  
ENV CONFD_VERSION 0.11.0  
ENV CONFD_URL
https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-
linux-amd64  
  
RUN wget --progress dot:mega $CONFD_URL -O /usr/local/bin/confd \  
&& chmod 755 /usr/local/bin/confd \  
&& mkdir -p /etc/confd/conf.d /etc/confd/templates  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY proxy.toml /etc/confd/conf.d/proxy.toml  
COPY proxy.tmpl /etc/confd/templates/proxy.tmpl  
  
EXPOSE 80  
EXPOSE 443  
CMD confd -onetime -backend env && /usr/local/nginx/sbin/nginx -c
/etc/nginx/nginx.conf  

