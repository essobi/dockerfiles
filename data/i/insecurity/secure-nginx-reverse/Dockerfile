FROM insecurity/secure-nginx:1.12.0-1  
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>  
# Base from https://hub.docker.com/r/woutertenbosch/nginx-reverse-proxy/  
  
# Set variables  
#ENV RUN_URL https://raw.githubusercontent.com/woutertenbosch/nginx-reverse-
proxy/master/run.sh  
#ENV CONF_URL https://raw.githubusercontent.com/woutertenbosch/nginx-reverse-
proxy/master/nginx.conf  
ENV CONF_URL https://bitbucket.org/jtof_fap/secure-
nginx/raw/master/Reverse/Compose/nginx.conf  
ENV REVERSE_DOMAIN example.com  
ENV REVERSE_PROTO http  
  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install -y --no-install-recommends \  
openssl \  
git \  
curl \  
  
# Replace configuration \  
&& mkdir -p /usr/local/bak/etc/ \  
&& cd /usr/local/bak/etc/ \  
&& wget $CONF_URL \  
&& chown nginx:nginx /usr/local/bak/etc/nginx.conf \  
&& cp /usr/local/bak/etc/nginx.conf /etc/nginx/nginx.conf \  
  
# Add run script \  
&& echo '#!/bin/bash' > /run.sh \  
&& echo 'echo "Configuring Nginx Reverse Proxy..."' >> /run.sh \  
&& echo 'cp -n /usr/local/bak/etc/nginx.conf /etc/nginx/nginx.conf' >> /run.sh
\  
&& echo 'sed -i "s/_REPLACE_ME_HOST_/$REVERSE_DOMAIN/g" /etc/nginx/nginx.conf'
>> /run.sh \  
&& echo 'sed -i "s/_REPLACE_ME_PROTO_/$REVERSE_PROTO/g" /etc/nginx/nginx.conf'
>> /run.sh \  
&& echo 'echo "Starting Nginx Reverse Proxy..."' >> /run.sh \  
&& echo 'exec /usr/sbin/nginx & tail -F /var/log/nginx/*' >> /run.sh \  
&& chmod 755 /run.sh \  
  
# APT Clean-up \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose and start  
EXPOSE 8080  
EXPOSE 8443  
CMD ["/run.sh"]  
  
  

