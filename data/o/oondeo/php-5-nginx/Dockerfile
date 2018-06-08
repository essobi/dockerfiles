FROM oondeo/php:5  
  
  
ENV SUMMARY="Nginx image with standar modules" \  
DESCRIPTION="The image use scripts and configurations compatible \  
with redhat openshift."  
  
LABEL summary="$SUMMARY" \  
description="$DESCRIPTION" \  
io.k8s.description="$DESCRIPTION" \  
io.k8s.display-name="Nginx" \  
io.openshift.s2i.scripts-url=image:///usr/libexec/s2i \  
io.s2i.scripts-url=image:///usr/libexec/s2i \  
com.redhat.component="nginx" \  
name="oondeo/php-5-nginx" \  
version="5" \  
release="6" \  
maintainer="OONDEO <info@oondeo.es>"  
# Docker Build Arguments  
ARG RESTY_CONFIG_OPTIONS=${RESTY_CONFIG_OPTIONS:-"\  
\--with-file-aio \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_geoip_module=dynamic \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module=dynamic \  
\--with-http_mp4_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_xslt_module=dynamic \  
\--with-ipv6 \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-md5-asm \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-threads \  
"  
ARG RESTY_CONFIG_OPTIONS_MORE=${RESTY_CONFIG_OPTIONS_MORE:-""}  
  
# 1) Install apt dependencies  
# 2) Download and untar OpenSSL, PCRE, and OpenResty  
# 3) Build OpenResty  
# 4) Cleanup  
USER root  
  
ADD s2i/bin $STI_SCRIPTS_PATH  
#ADD nginx/scripts $STI_SCRIPTS_PATH  
  
RUN $STI_SCRIPTS_PATH/build \  
&& mv /usr/local/openresty/nginx /opt/app-root/ \  
&& ln -sf /opt/app-root/nginx /usr/local/openresty/nginx  
  
#sed -i 's/var.log.nginx/opt\/app-root\/nginx\/logs/g' default.conf  
RUN ln -sf /opt/app-root/nginx/conf /etc/nginx \  
&& ln -sf /opt/app-root/nginx/logs /var/log/nginx \  
&& apt-get update && apt-get install --no-install-recommends -y runit \  
&& DEBIAN_FRONTEND=noninteractive apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/* /var/log/* /usr/share/doc/* /usr/share/man/* /root/.cache  
# Add additional binaries into PATH for convenience  
ENV
PATH=$PATH:/usr/local/sbin:/usr/local/openresty/luajit/bin/:/usr/local/openresty/nginx/sbin/:/usr/local/openresty/bin/  
#This is needed in development  
ENV NGINXCONF_FASTCGI_READ_TIMEOUT=3600 \  
NGINX_CACHE=0  
  
ADD nginx/common /opt/app-root/nginx/conf  
ADD services.d /opt/app-root/etc/service  
  
  
# Reset permissions of modified directories and add default user  
RUN useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin \  
-c "Default Application User" default || true  
RUN chown -R 1001:0 /opt/app-root \  
&& ln -sf /opt/app-root/nginx/logs /var/log/nginx \  
&& chmod -R g+w /opt/app-root \  
&& chmod ug+s /opt/app-root/* \  
&& mkdir -p ${HOME}/.pki/nssdb \  
&& chown -R 1001:0 ${HOME}/.pki \  
&& chmod 775 /var/run && chmod 775 /run \  
&& chmod ug+s /run /var/run \  
&& chown 1001 /var/run /run  
  
  
EXPOSE 8080 8081 9000  
  
CMD [ "/usr/bin/runsvdir", "/opt/app-root/etc/service" ]  
  
USER 1001  

