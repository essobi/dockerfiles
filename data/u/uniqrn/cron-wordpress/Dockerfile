FROM wordpress:php7.1-apache  
LABEL maintainer "unicorn research Ltd."  
  
RUN apt-get update && apt-get install -y --no-install-recommends git cron \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY pam-cron /etc/pam.d/cron  
  
# cron startup & apache2 up  
RUN mv /usr/local/bin/docker-entrypoint.sh /usr/local/bin/docker-
entrypoint.sh.bak \  
&& awk '{print $0 ((NR==3)?"\nservice cron start\n":"")}'
/usr/local/bin/docker-entrypoint.sh.bak > /usr/local/bin/docker-entrypoint.sh
\  
&& chmod +x /usr/local/bin/docker-entrypoint.sh  

