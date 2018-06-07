FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
bind9-host \  
cron \  
curl \  
git \  
inotify-tools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
&& git clone https://github.com/Neilpang/acme.sh.git \  
&& cd acme.sh \  
&& ./acme.sh --install \  
\--home /usr/bin \  
\--certhome /var/certs  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT [ "/entrypoint.sh" ]  

