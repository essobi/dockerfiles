FROM ubuntu:xenial  
MAINTAINER romeOz <serggalka@gmail.com>  
  
ENV OS_LOCALE="en_US.UTF-8"  
RUN apt-get update && apt-get install -y locales && locale-gen ${OS_LOCALE}  
ENV LANG=${OS_LOCALE} \  
LANGUAGE=en_US:en \  
LC_ALL=${OS_LOCALE}  
  
RUN \  
buildDeps='wget' \  
&& apt-get install --no-install-recommends -y $buildDeps \  
&& wget -O - http://nginx.org/keys/nginx_signing.key | apt-key add \- \  
&& echo "deb http://nginx.org/packages/ubuntu/ xenial nginx" | tee -a
/etc/apt/sources.list \  
&& echo "deb-src http://nginx.org/packages/ubuntu/ xenial nginx" | tee -a
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y nginx \  
# Cleaning  
&& apt-get purge -y \--auto-remove $buildDeps locales \  
&& apt-get autoremove -y && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
# Forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY ./configs/nginx.conf /etc/nginx/nginx.conf  
  
WORKDIR /var/www  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]

