FROM ubuntu:16.04  
MAINTAINER Tran Duc Thang <thangtd90@gmail.com>  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
ENV DEBIAN_FRONTEND=noninteractive  
  
COPY nginx-common_1.10.0-0ubuntu0.16.04.4-postgres_all.deb /tmp/nginx-
common_1.10.0-0ubuntu0.16.04.4-postgres_all.deb  
COPY nginx-full_1.10.0-0ubuntu0.16.04.4-postgres_amd64.deb /tmp/nginx-
full_1.10.0-0ubuntu0.16.04.4-postgres_amd64.deb  
COPY libssl1.0.2_1.0.2j-4_amd64.deb /tmp/libssl1.0.2_1.0.2j-4_amd64.deb  
  
RUN apt-get update && apt-get install -y apt-utils libpq5 libexpat1 libgd3
libgeoip1 libxml2 libxslt1.1  
  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
RUN apt-get upgrade -y  
  
RUN yes | dpkg -i /tmp/libssl1.0.2_1.0.2j-4_amd64.deb /tmp/nginx-
common_1.10.0-0ubuntu0.16.04.4-postgres_all.deb /tmp/nginx-
full_1.10.0-0ubuntu0.16.04.4-postgres_amd64.deb  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY upstream.conf /etc/nginx/conf.d/upstream.conf  
RUN usermod -u 1000 www-data  
  
CMD ["nginx", "-g", "daemon off;"]  
  
EXPOSE 80 8081  

