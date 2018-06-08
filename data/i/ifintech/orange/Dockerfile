FROM centos:7  
MAINTAINER luogreen, luogreen@foxmail.com  
  
# Docker Build Arguments, For further upgrade  
ENV ORANGE_PATH="/usr/local/orange"  
ARG LOR_VERSION="0.3.2"  
ENV ORANGE_VERSION="0.6.4"  
  
RUN \  
yum-config-manager --add-repo
https://openresty.org/yum/cn/centos/OpenResty.repo \  
&& yum install -y epel-release \  
&& yum install -y openresty openresty-resty make telnet \  
  
&& yum clean all \  
  
&& ln -s /usr/local/openresty/nginx/sbin/nginx /usr/local/bin/nginx \  
  
&& cd /tmp \  
&& curl -fSL https://github.com/sumory/lor/archive/v${LOR_VERSION}.tar.gz -o
lor.tar.gz \  
&& tar zxf lor.tar.gz \  
&& cd /tmp/lor-${LOR_VERSION} \  
&& make install \  
  
&& cd /tmp \  
&& curl -fSL
https://github.com/sumory/orange/archive/v${ORANGE_VERSION}.tar.gz -o
orange.tar.gz \  
&& tar zxf orange.tar.gz \  
&& cd orange-${ORANGE_VERSION} \  
&& make install \  
  
&& cd / \  
&& rm -rf /tmp/* \  
  
&& useradd www \  
&& echo "www:www" | chpasswd \  
&& echo "www ALL=(ALL) ALL" >> /etc/sudoers \  
&& mkdir -p ${ORANGE_PATH}/logs \  
&& chown -R www:www ${ORANGE_PATH}/*  
  
  
ADD docker-entrypoint.sh docker-entrypoint.sh  
RUN chmod 755 docker-entrypoint.sh && mv docker-entrypoint.sh /usr/local/bin  
  
EXPOSE 7777 80 9999 83  
  
COPY nginx.conf /usr/local/orange/conf/nginx.conf  
  
# Daemon  
ENTRYPOINT ["docker-entrypoint.sh"]  

