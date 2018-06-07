# consup_nginx  
# Consup nginx image  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_baseapp  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION_NGINX 170429  
#
-------------------------------------------------------------------------------  
# Run custom setup scripts  
ADD setup_*.sh /tmp/  
RUN for f in /tmp/setup_*.sh ; do >&2 echo ">>>> $f" ; . $f ; rm $f ; done  
  
#
-------------------------------------------------------------------------------  
# disables nginx remove  
# VOLUME ["/var/cache/nginx"]  
# default nginx log destination  
VOLUME ["/var/log/nginx"]  
  
EXPOSE 80 443  
COPY init.d /init.d  
COPY consul /etc/consul  
COPY supervisor.d /etc/supervisor/conf.d  
COPY skel /skel  
  
ADD fastcgi_params /etc/nginx/  
ADD proxy_params /etc/nginx/  
ADD ssl.conf /etc/nginx/  
ADD acme_mgr.sh /etc/nginx/  
  
# ------------------------------------------------------------  
# Frontend server config  
# Consul upstreams domain for service named "web"  
ENV CONSUL_DOMAIN web.service.consul  
  
# Redirect 502 errors  
#ENV NGINX_DEFAULT http://localhost/maintenance.html  
# This will be used if NGINX_DEFAULT not set  
COPY nohost.html /usr/share/nginx/html/nohost.html  
  
# Used in /etc/consul/src/nginx-redir.conf  
ENV NGINX_REDIR "http://www.localhost"  
# Use frontend config in this MODE  
# (see init.d/setup_nginx.sh)  
ENV FRONT_MODE common  
  
# Use redirect config in this MODE  
# (see init.d/setup_nginx.sh)  
ENV REDIR_MODE redir  
  
# Use proxy config in this MODE  
# (see init.d/setup_nginx.sh)  
ENV PROXY_MODE proxy  
  
# Register this service in consul  
ENV SERVICE webfront  
  
# ------------------------------------------------------------  
# Backend server config (FRONT_MODE != common, SERVICE == web)  
# nginx server name  
ENV NODENAME demo.consul  
  
# Document root = $HTML_ROOT/$HTML_DIR  
ENV HTML_ROOT /home/app  
ENV HTML_DIR html  

