FROM nginx:1.13.12  
LABEL maintainer "Erwin Mueller <erwin.mueller@deventm.com>"  
  
ARG APT_CACHE  
  
RUN set -x \  
# Optional add proxy entries for apt.  
&& if [ -n "${APT_CACHE}" ]; then \  
echo Acquire::ftp::Proxy \"$APT_CACHE\"; >> /etc/apt/apt.conf.d/08proxy;\  
echo Acquire::http::Proxy \"$APT_CACHE\"; >> /etc/apt/apt.conf.d/08proxy;\  
echo Acquire::https::Proxy \"$APT_CACHE\"; >> /etc/apt/apt.conf.d/08proxy;\  
fi  
  
RUN set -x \  
&& DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
rsync \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD rootfs/ /  
  
RUN set -x \  
&& chmod +x /*.sh \  
&& mkdir -p /var/cache/nginx \  
# Set permissions.  
&& chown nginx.root -R /etc/nginx \  
&& chmod u=rwX,g=rwX,o=rX -R /etc/nginx \  
&& chown nginx.root -R /var/cache/nginx \  
&& chmod u=rwX,g=rwX,o=rX -R /var/cache/nginx \  
&& mkdir -p /run/nginx \  
&& chown nginx.root -R /run/nginx \  
&& chmod u=rwX,g=rwX,o=rX -R /run/nginx\  
&& chown nginx.root -R /var/log/nginx \  
&& chmod u=rwX,g=rwX,o=rX -R /var/log/nginx  
  
ENV WEB_ROOT="/var/www/html" \  
NGINX_HTTP_PORT="8080" \  
NGINX_HTTPS_PORT="8443"  
  
WORKDIR ${WEB_ROOT}  
  
# http, https  
EXPOSE 8080  
EXPOSE 8443  
  
USER nginx  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  

