# Nginx  
#  
# HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP  
# proxy server  
FROM winggundamth/ubuntu-base:xenial  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=xenial-20160809  
# 1) Install Nginx  
# 2) Install Python because it required by Ansible  
# 3) Clean to reduce Docker Image size  
ARG APT_CACHER_NG  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu \  
$(lsb_release -cs) main" \  
> /etc/apt/sources.list.d/nginx-$(lsb_release -cs).list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C && \  
apt-get update && \  
apt-get install -y nginx-extras python && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy  
  
# 1) Config Nginx not to run as daemon but foreground instead  
RUN sed -i "/pid .*/a \daemon off;" /etc/nginx/nginx.conf  
  
EXPOSE 80 443  
VOLUME ["/var/log", "/etc/nginx", "/etc/ssl/private"]  
CMD ["nginx"]  

