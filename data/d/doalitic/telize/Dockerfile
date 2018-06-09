FROM jess/telize:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
supervisor \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN apt-get update && apt-get install -y \  
cron \  
curl \  
wget \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
COPY update-geodb.cron /etc/cron.d/update-geodb  
COPY update-geodb.sh /root/update-geodb.sh  
COPY telize.conf /etc/nginx/conf.d/telize.conf  
  
EXPOSE 443  
# The following environment variables are available:  
#  
# NGINX_SSL_CERTIFICATE nginx ssl certificate content (optional)  
# NGINX_SSL_KEY nginx ssl private key content (optional)  
#  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.0.4/dockerize-linux-
amd64-v0.0.4.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.0.4.tar.gz \  
&& rm -f dockerize-linux-amd64-v0.0.4.tar.gz  
ADD ./server.key.tpl /etc/container/templates/  
ADD ./server.crt.tpl /etc/container/templates/  
  
ENTRYPOINT ["dockerize"]  
  
CMD ["-template",
"/etc/container/templates/server.key.tpl:/etc/ssl/private/server.key", \  
"-template",
"/etc/container/templates/server.crt.tpl:/etc/ssl/private/server.crt", \  
"supervisord"]  

