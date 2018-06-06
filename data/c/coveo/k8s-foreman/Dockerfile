FROM ubuntu:16.04  
LABEL maintainer "coveo"  
  
# Config for Foreman  
ENV FOREMAN_RELEASE 1.15  
ENV FOREMAN_VERSION 1.15.0-1  
# Install Supervisor  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor cron git golang  
  
# Create puppet user and group with defined UID and GID  
RUN useradd -u 1000 -U puppet  
  
# Install Foreman-Installer  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget && \  
wget -q https://deb.theforeman.org/pubkey.gpg -O- | apt-key add - && \  
echo "deb http://deb.theforeman.org/ xenial $FOREMAN_RELEASE" >
/etc/apt/sources.list.d/foreman.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
foreman-installer tzdata  
  
# Install Foreman-plugin  
RUN echo "deb http://deb.theforeman.org/ plugins $FOREMAN_RELEASE" >
/etc/apt/sources.list.d/foreman-plugins.list && \  
apt-get update  
  
# Prerequisite for EFS  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nfs-common && \  
mkdir /install && \  
mkdir -p /var/lib/puppet/ssl  
  
# make hostname -f work for foreman-installer  
RUN rm -f /usr/share/foreman-installer/checks/hostname.rb && export
FACTER_fqdn="$HOSTNAME.docker.local"  
  
RUN foreman-installer \  
\--foreman-version=$FOREMAN_VERSION \  
\--foreman-db-type=mysql \  
\--foreman-db-manage=false \  
\--foreman-db-manage-rake=false \  
\--foreman-proxy-puppet=false \  
\--foreman-proxy-puppetca=false \  
\--enable-foreman-plugin-default-hostgroup \  
\--no-enable-foreman-proxy \  
\--no-enable-puppet \  
\--foreman-ssl=false && \  
service foreman stop && \  
service apache2 stop && \  
systemctl disable foreman && \  
systemctl disable apache2  
  
# Clean apt cache  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY files/install /install  
RUN chmod +x /install/*.sh  
RUN /install/json_exporter.sh  
  
COPY files/supervisord /etc/supervisor  
COPY files/foreman/prometheus.rake
/usr/share/foreman/lib/tasks/prometheus.rake  
COPY files/exporter_config.yaml /prometheus/prometheus-json-
exporter/config.yaml  
  
EXPOSE 443  
EXPOSE 7979  
ENTRYPOINT ["/install/entrypoint.sh"]  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

