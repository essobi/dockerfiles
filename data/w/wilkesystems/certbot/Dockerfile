FROM debian:stretch-slim  
  
MAINTAINER wilkesystems <maintainer@wilke.systems>  
  
RUN apt-get update; \  
echo "exim4-config exim4/mailname string $(hostname --fqdn)" | debconf-set-
selections; \  
echo "exim4-config exim4/dc_postmaster string postmaster@$(hostname --fqdn)" |
debconf-set-selections; \  
apt-get install -y cron curl exim4-daemon-light letsencrypt locales locales-
all supervisor; \  
curl -sSL https://get.docker.com/ | sh > /dev/null 2>&1; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ["docker-entrypoint.sh", "/usr/bin/docker-entrypoint.sh"]  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

