FROM gcr.io/google_containers/ubuntu-slim:0.14  
MAINTAINER Presslabs <ping@presslabs.com>  
  
ENV NGINX_PACKAGE_VERSION 1.10.3-xenial~ppa20170206.0  
  
# Disable prompts from apt.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Do not split this into multiple RUN!  
# Docker creates a layer for every RUN-Statement  
# therefore an 'apt remove --purge -y build*' has no effect  
RUN set -ex \  
&& apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys
15E2F69969F5EF4F46F14A02C9247EBC3EE61981 \  
&& echo deb http://ppa.launchpad.net/presslabs/ppa/ubuntu xenial main >
'/etc/apt/sources.list.d/presslabs.list' \  
&& apt-get update -y \  
&& apt-get install -y \--no-install-recommends ca-certificates nginx-
full=$NGINX_PACKAGE_VERSION \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& rm -rf /etc/nginx/sites-enabled \  
&& rm -rf /etc/nginx/sites-available \  
&& rm -rf /usr/share/man /usr/share/doc /var/lib/apt/lists/*
/var/cache/apt/archives/*  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

