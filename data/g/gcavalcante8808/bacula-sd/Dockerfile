FROM debian:8  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install -qqy --no-install-recommends \  
ca-certificates curl && \  
curl -L "https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64" -o /usr/local/bin/dumb-init && \  
chmod +x /usr/local/bin/dumb-init  
RUN apt-get install -qqy --no-install-recommends bacula-sd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY files/bacula-sd.conf.j2 /etc/bacula/bacula-sd.conf  
COPY files/docker-entrypoint.sh /  
ENTRYPOINT ["/usr/local/bin/dumb-init","/docker-entrypoint.sh"]  
  

