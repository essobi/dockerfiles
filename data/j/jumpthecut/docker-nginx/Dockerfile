#  
# Nginx Dockerfile  
#  
# Pull base image  
FROM ubuntu:14.04  
# User limits  
RUN sed -i.bak '/\\# End of file/ i\\\\# Following 4 lines added by docker-
couchbase-server' /etc/security/limits.conf  
RUN sed -i.bak '/\\# End of file/ i\\\\* hard memlock unlimited'
/etc/security/limits.conf  
RUN sed -i.bak '/\\# End of file/ i\\\\* soft memlock unlimited\n'
/etc/security/limits.conf  
RUN sed -i.bak '/\\# End of file/ i\\\\* hard nofile 65536'
/etc/security/limits.conf  
RUN sed -i.bak '/\\# End of file/ i\\\\* soft nofile 65536\n'
/etc/security/limits.conf  
RUN sed -i.bak '/\\# end of pam-auth-update config/ i\\\\# Following line was
added by docker-couchbase-server' /etc/pam.d/common-session  
RUN sed -i.bak '/\\# end of pam-auth-update config/ i\session required
pam_limits.so\n' /etc/pam.d/common-session  
  
# Locale  
RUN locale-gen en_US en_US.UTF-8  
  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install vim wget curl bridge-utils build-essential libpcre3
libpcre3-dev libpcrecpp0 libssl-dev zlib1g-dev logrotate cron && \  
wget 'https://github.com/openresty/headers-more-nginx-
module/archive/v0.261.tar.gz' && \  
wget 'http://nginx.org/download/nginx-1.8.0.tar.gz' && \  
wget 'https://raw.githubusercontent.com/JasonGiedymin/nginx-init-
ubuntu/master/nginx' -O /etc/init.d/nginx && \  
tar -xzvf v0.261.tar.gz && \  
tar -xzvf nginx-1.8.0.tar.gz && \  
cd nginx-1.8.0/ && \  
./configure --sbin-path=/usr/sbin --with-http_ssl_module --add-
module=../headers-more-nginx-module-0.261 && \  
make && \  
make install && \  
cd /usr/local/bin && \  
curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 -o confd && \  
chmod +x confd && \  
cron && \  
mkdir -p /etc/nginx/sites-enabled && \  
mkdir -p /etc/confd/conf.d && \  
mkdir -p /etc/confd/templates  
  
RUN /usr/sbin/update-rc.d cron defaults  
RUN rm -f /etc/nginx/sites-enabled/default  
RUN rm -f /etc/nginx/nginx.conf  
RUN chmod +x /etc/init.d/nginx  
RUN /usr/sbin/update-rc.d -f nginx defaults  
  
ADD nginx.toml /etc/confd/conf.d/nginx.toml  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD confd-watch /usr/local/bin/confd-watch  
RUN chmod 755 /usr/local/bin/confd-watch  
RUN chmod -R +rwx /usr/local/nginx  
RUN chown -R www-data /usr/local/nginx  
  
# Expose port  
EXPOSE 80 443  
# start couchbase  
CMD ["/bin/bash"]  

