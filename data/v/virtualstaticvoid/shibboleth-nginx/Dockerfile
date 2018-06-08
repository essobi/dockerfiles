  
FROM debian:wheezy  
  
# See https://github.com/nginx-shib/nginx-http-
shibboleth/blob/master/CONFIG.rst  
RUN echo "deb http://http.debian.net/debian wheezy-backports main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y -t \  
wheezy-backports \  
opensaml2-schemas \  
xmltooling-schemas \  
libshibsp6 \  
libshibsp-plugins \  
shibboleth-sp2-common \  
shibboleth-sp2-utils \  
supervisor \  
procps \  
curl \  
git \  
build-essential \  
libpcre3 \  
libpcre3-dev \  
libpcrecpp0 \  
libssl-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Copy supervisor config files  
COPY supervisor /etc/supervisor  
  
# Copy shibboleth config directory  
COPY shibboleth /etc/shibboleth  
  
# Build and install nginx  
ADD ./build-nginx.sh /tmp/build-nginx.sh  
RUN /bin/bash /tmp/build-nginx.sh  
  
# Copy nginx config files  
COPY nginx /etc/nginx  
  
# Forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Create missing dirs and generate shibboleth keys  
RUN mkdir /var/run/shibboleth /var/log/shibboleth /var/cache/nginx || true &&
shib-keygen -f  
  
# Set permissions  
RUN chown -R _shibd /var/log/nginx /var/cache/nginx  
  
# Get envplate  
# @see https://github.com/kreuzwerker/envplate  
RUN curl -sLo /usr/local/bin/ep
https://github.com/kreuzwerker/envplate/releases/download/v0.0.7/ep-linux \  
&& chmod +x /usr/local/bin/ep  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["/usr/local/bin/ep", "-v", "/etc/nginx/conf.d/default.conf",
"/etc/shibboleth/shibboleth2.xml", "--", "/usr/bin/supervisord", "--nodaemon",
"--configuration", "/etc/supervisor/supervisord.conf"]  

