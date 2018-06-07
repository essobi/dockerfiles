FROM debian:jessie  
MAINTAINER Hellyna NG <hellyna@groventure.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y --no-install-recommends \  
# Requires by check-memory-percent  
bc \  
build-essential \  
ca-certificates \  
curl && \  
curl -L 'http://repos.sensuapp.org/apt/pubkey.gpg' | apt-key add - && \  
echo 'deb http://repos.sensuapp.org/apt sensu main' >
/etc/apt/sources.list.d/sensu.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
sensu && \  
chown -Rv sensu:sensu /opt/sensu/ && \  
/opt/sensu/embedded/bin/gem install --no-rdoc \  
sensu-plugins-cpu-checks \  
sensu-plugins-disk-checks \  
sensu-plugins-memory-checks \  
sensu-plugins-network-checks \  
sensu-plugins-mailer && \  
apt-get purge -y \  
build-essential \  
ca-certificates \  
curl && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rvf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
COPY conf/* /etc/sensu/conf.d/  
COPY templates/* /docker-templates/  
RUN mkdir -pv /etc/sensu/plugins/ && \  
chown -Rv sensu:sensu /etc/sensu/plugins/ && \  
chmod -Rv 0700 /etc/sensu/plugins/ && \  
chown -R sensu:sensu /docker-templates /etc/sensu/conf.d && \  
chmod 0700 /docker-templates /etc/sensu/conf.d && \  
chmod 0600 /docker-templates/* /etc/sensu/conf.d/*  
  
COPY scripts/entrypoint.sh /docker-scripts/  
  
VOLUME ["/etc/sensu", "/docker-templates"]  
  
USER sensu  
  
ENTRYPOINT ["/bin/bash", "/docker-scripts/entrypoint.sh"]  

