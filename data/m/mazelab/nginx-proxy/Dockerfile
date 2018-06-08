FROM nginx:1.9.3  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
# rm default conf data from parent image  
RUN rm -rf /etc/nginx/*  
  
# Install packages  
RUN apt-get update -y -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-
recommends \  
# ssl support  
ca-certificates \  
# download support  
wget \  
# scheduler support  
cron \  
# editing support  
nano \  
&& apt-get clean -y -qq \  
&& apt-get autoremove -y -qq \  
&& rm -r /var/lib/apt/lists/*  
  
# Install Forego  
RUN wget -P /usr/local/bin -q
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego \  
&& chmod u+x /usr/local/bin/forego  
  
# Set docker gen version to use  
ENV DOCKER_GEN_VERSION 0.7.0  
# Install Docker-Gen  
RUN wget -q https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
# Add content early as modified less often  
ADD ./container-data/Procfile /app/  
ADD ./container-data/mime.types /etc/nginx/  
ADD ./container-data/nginx.conf /etc/nginx/  
ADD ./container-data/prepare.sh /up/prepare.sh  
ADD ./container-data/rotate_nginx_log.sh /usr/local/sbin/rotate_nginx_log.sh  
  
ENV TERM xterm  
  
# Choose the template to run, you may use dev for experimental use  
ENV GLOB_TMPL_MODE run  
# Set max size within a body  
ENV GLOB_MAX_BODY_SIZE 10m  
  
# Enable bundle support to provide nginx CA chain.  
# Have a look at
http://nginx.org/en/docs/http/configuring_https_servers.html#chains for more
info.  
ENV GLOB_SSL_CERT_BUNDLE_INFIX ""  
# Set default session timeout  
ENV GLOB_SSL_SESSION_TIMEOUT 5m  
  
# Set default shared session cache  
ENV GLOB_SSL_SESSION_CACHE 50m  
  
# Enable OCSP through setting this value to any > 0.  
# See http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_stapling  
ENV GLOB_SSL_OCSP_VALID_TIME "0"  
# DNS servers to resolve the certificate verification from. Unused if
GLOB_SSL_OCSP_VALID_TIME <= 0  
# Uses OpenNicProject server first and will fall back to google one's. You can
use only google's as well with "8.8.4.4 8.8.8.8"  
ENV GLOB_SSL_OCSP_DNS_ADDRESSES "5.9.49.12 8.8.8.8"  
# Timeout when verifying certificates. Unused if GLOB_SSL_OCSP_VALID_TIME <= 0  
ENV GLOB_SSL_OCSP_DNS_TIMEOUT "10s"  
# Only allow ssl  
ENV GLOB_SSL_FORCE "1"  
# Control SPDY support  
# More info https://www.mare-system.de/guide-to-nginx-ssl-spdy-hsts/  
ENV GLOB_SPDY_ENABLED "0"  
# Default return code for errors  
ENV GLOB_HTTP_NO_SERVICE 503  
# Redirect prefixed to non prefix (e.g. 'http://WWW.xyz.io' to
'http://xyz.io')  
ENV GLOB_AUTO_REDIRECT_ENABLED "0"  
# Set prefix to be used for auto redirect  
ENV GLOB_AUTO_REDIRECT_PREFIX www  
  
# set direction  
# - 0: redirect from prefix to non-prefix (e.g. 'http://WWW.xyz.io' to
'http://xyz.io')  
# - 1: redirect from non-prefix to prefix (e.g. 'http://xyz.io' to
'http://API.xyz.io')  
ENV GLOB_AUTO_REDIRECT_DIRECTION "0"  
# User to run the proxy  
ENV GLOB_USER_NAME nginx  
  
# Multilevel proxy cache  
ENV GLOB_CACHE_ENABLE "1"  
# Define the amount of workers nginx should use  
ENV GLOB_WORKER_COUNT auto  
  
# Limit the maximum amount of total connections  
ENV GLOB_WORKER_CONNECTIONS 256  
# Allow each worker to process multiple connections at once  
ENV GLOB_WORKER_MULTI_ACCEPT on  
  
# Set the maximum open file handles of each worker  
ENV GLOB_WORKER_RLIMIT_NOFILE 1024  
# Set the default error log level  
ENV GLOB_ERROR_LOG_LEVEL error  
  
# Time the server keeps the connection active without request from client  
ENV GLOB_KEEPALIVE_TIMEOUT 0  
# Number of idle connections to upstream services to keep and don't waste time
for TCP handshaking etc.  
ENV GLOB_UPSTREAM_IDLE_CONNECTIONS 0  
# Define the maximum amount of connections per IP to allowed  
ENV GLOB_LIMIT_CONS_PER_IP 50  
# Define the peak amount of requests per connection allowed.  
ENV GLOB_LIMIT_REQS_BURST 80  
# Allow CORS anywhere globally  
ENV GLOB_WILD_CORS "0"  
# Connect to docker host via socket by default  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
# Set custom ssl redirect port  
ENV GLOB_SSL_REDIRECT_PORT ""  
# define proxy read timeout in seconds  
ENV GLOB_PROXY_READ_TIMEOUT 420  
RUN chmod a+x /up/prepare.sh && bash ./up/prepare.sh  
RUN rm -rf /up  
  
# Configure and schedule log rotation  
RUN chmod +x /usr/local/sbin/rotate_nginx_log.sh  
RUN mkdir -p /etc/cron.d  
RUN echo "* 1 * * * /usr/local/sbin/rotate_nginx_log.sh" >>
/etc/cron.d/nginx_log  
  
# Change to working directory  
WORKDIR /app/  
  
ADD ./docker-entrypoint.sh /app/docker-entrypoint.sh  
  
# Add late, as tmpl is most modified part and less content needs to be rebuilt  
ADD ./container-data/nginx-${GLOB_TMPL_MODE}.tmpl ./nginx.tmpl  
  
VOLUME
["/etc/nginx/certs","/etc/nginx/htpasswd","/etc/nginx/vhost.d/","/etc/nginx/conf.d/","/var/log/nginx"]  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["forego", "start", "-r"]  

