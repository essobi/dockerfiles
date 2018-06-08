FROM debian:jessie  
MAINTAINER thaim <thaim24@gmail.com>  
  
  
RUN apt-get update && apt-get install -y 'ca-certificates' \--no-install-
recommends  
  
ENV NGINX_VERSION=1.11.1 \  
CONTAINER_BUILD_VERSION=0  
COPY configure.sh configure.sh  
COPY modules3rd.ini modules3rd.ini  
  
RUN buildDeps='\  
golang \  
git \  
wget \  
build-essential \  
libpcre3-dev \  
zlib1g-dev \  
libperl-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libgd-dev \  
libgeoip-dev \  
'\  
&& export GOPATH="/root/.go" \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& mkdir $GOPATH work /var/log/nginx /var/lib/nginx \  
&& go get -u github.com/cubicdaiya/nginx-build  
  
RUN /root/.go/bin/nginx-build -d work -m modules3rd.ini -c configure.sh -clear
\  
&& cd /work/nginx/${NGINX_VERSION}/nginx-${NGINX_VERSION} \  
&& make install \  
&& rm -rf /work /root/.go /modules3rd.ini /configure.sh \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

