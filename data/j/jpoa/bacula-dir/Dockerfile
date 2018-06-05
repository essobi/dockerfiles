FROM debian:9  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install -qqy --no-install-recommends \  
ca-certificates curl && \  
curl -L "https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64" -o /usr/local/bin/dumb-init && \  
chmod +x /usr/local/bin/dumb-init  
RUN apt-get install -qqy --no-install-recommends bacula-director-pgsql bacula-
console mtx mt-st && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY files/docker-entrypoint.sh /  
COPY files/bacula-dir.conf.j2 /etc/bacula/bacula-dir.conf  
COPY files/bconsole.conf.j2 /etc/bacula/bconsole.conf  
  
ENTRYPOINT ["/usr/local/bin/dumb-init","/docker-entrypoint.sh"]  

