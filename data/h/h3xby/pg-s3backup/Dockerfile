FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends awscli postgresql-client cron \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV CRON_CONFIG '0 1 * * *'  
ADD bin /usr/local/bin/  
  
CMD ["mycron"]  

