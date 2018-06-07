# modperl meta dockerfile  
# See https://github.com/LeKovr/consup  
FROM debian:wheezy  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV CONSUP_UBUNTU_CODENAME wheezy  
  
ENV DOCKERFILE_VERSION 160320  
#
-------------------------------------------------------------------------------  
# **** base ****  
#
-------------------------------------------------------------------------------  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
  
#
-------------------------------------------------------------------------------  
# Run custom setup scripts  
ADD setup_*.sh /tmp/  
  
# Loop does not cache every step  
#RUN for f in /tmp/setup_*.sh ; do >&2 echo ">>>> $f" ; . $f ; rm $f ; done  
RUN bash /tmp/setup_0backports.sh  
RUN bash /tmp/setup_1pkg.sh  
RUN bash /tmp/setup_2pgdg.sh  
RUN bash /tmp/setup_consul.sh  
RUN bash /tmp/setup_consul-tmpl.sh  
RUN bash /tmp/setup_dbinit.sh  
RUN bash /tmp/setup_gosu.sh  
RUN bash /tmp/setup_lang.sh  
RUN bash /tmp/setup_nginx.sh  
RUN bash /tmp/setup_perl.sh  
RUN bash /tmp/setup_perllib_debian.sh  
RUN bash /tmp/setup_pg_client.sh  
  
#
-------------------------------------------------------------------------------  
# Run init.d.sh on boot before supervisor  
COPY init.d /init.d  
COPY init.d.sh /  
CMD ["/init.d.sh", "supervisord", "-c", "/etc/supervisor/supervisord.conf",
"-n" ]  
  
#
-------------------------------------------------------------------------------  
# supervisor staff  
COPY supervisord.conf /etc/supervisor/  
VOLUME ["/var/run/supervisor", "/var/log/supervisor"]  
  
#
-------------------------------------------------------------------------------  
# Setup primary lang  
ENV LANG en_US.UTF-8  
# Default timezone  
ENV TZ Europe/Moscow  
  
#
-------------------------------------------------------------------------------  
# **** baseapp  
#
-------------------------------------------------------------------------------  
COPY supervisor.d /etc/supervisor/conf.d  
COPY consul /etc/consul  
  
# consul server's ip or hostname  
ENV CONSUL_MASTER consul  
  
# consul resolver  
ENV DNS_MASTER 8.8.8.8  
#
-------------------------------------------------------------------------------  
# **** nginx ****  
#
-------------------------------------------------------------------------------  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
ADD fastcgi_params /etc/nginx/  
ADD proxy_params /etc/nginx/  
# ADD ssl.conf /etc/nginx/  
# ------------------------------------------------------------  
# Frontend server config  
# Consul upstreams domain for service named "web"  
ENV CONSUL_DOMAIN web.service.consul  
  
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
ENV SERVICE web  
  
# ------------------------------------------------------------  
# Backend server config (FRONT_MODE != common, SERVICE == web)  
# nginx server name  
ENV NODENAME demo.consul  
  
# Document root = $HTML_ROOT/$HTML_DIR  
ENV HTML_ROOT /home/app  
ENV HTML_DIR html  
  
#
-------------------------------------------------------------------------------  
# **** pgws ****  
#
-------------------------------------------------------------------------------  
WORKDIR /home/app  
  
#
-------------------------------------------------------------------------------  
# **** modperl ****  
#
-------------------------------------------------------------------------------  
# Install apache-1.3.42 & mod_perl-1.31  
COPY asset-apache/*.deb /opt/apache/  
RUN cd /opt/apache && dpkg -i *.deb  

