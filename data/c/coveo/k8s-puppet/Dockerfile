FROM ubuntu:16.04  
LABEL maintainer "coveo"  
  
# Config for Puppet  
ENV PUPPETMASTER_SERVER_VERSION 3.8.5  
# Config for Foreman  
ENV FOREMAN_RELEASE 1.15  
ENV FOREMAN_PROXY_VERSION 1.15.0-1  
# CVE-2017-9445  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y systemd  
  
# Install Supervisor  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor augeas-tools  
  
# Create puppet user and group with defined UID and GID  
RUN useradd -u 1000 -U puppet  
  
# Install Foreman-Installer  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget && \  
wget -q https://deb.theforeman.org/pubkey.gpg -O- | apt-key add - && \  
echo "deb http://deb.theforeman.org/ xenial $FOREMAN_RELEASE" >
/etc/apt/sources.list.d/foreman.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
foreman-installer tzdata cron  
  
# Install Foreman-plugin  
RUN echo "deb http://deb.theforeman.org/ plugins $FOREMAN_RELEASE" >
/etc/apt/sources.list.d/foreman-plugins.list && \  
apt-get update  
  
# make hostname -f work for foreman-installer  
RUN rm -f /usr/share/foreman-installer/checks/hostname.rb && export
FACTER_fqdn="$HOSTNAME.docker.local"  
RUN foreman-installer \  
\--foreman-proxy-version=$FOREMAN_PROXY_VERSION \  
\--puppet-server-version=$PUPPETMASTER_SERVER_VERSION-2ubuntu0.1 \  
\--no-enable-foreman \  
\--no-enable-foreman-cli \  
\--no-enable-foreman-plugin-bootdisk \  
\--no-enable-foreman-plugin-setup \  
\--foreman-proxy-tftp=false \  
\--foreman-proxy-dhcp=false \  
\--foreman-proxy-dns=false \  
\--enable-puppet \  
\--puppet-server-passenger=true \  
\--puppet-server-passenger-min-instances=4 \  
\--puppet-agent=false \  
\--puppet-server-foreman-url=https://foreman.example.com \  
\--enable-foreman-proxy \  
\--foreman-proxy-tftp=false \  
\--foreman-proxy-register-in-foreman=false \  
\--foreman-proxy-dhcp-option-domain="" \  
\--foreman-proxy-dns-zone="" \  
\--puppet-srv-domain="" ; exit 0  
  
# Disable Services  
RUN service foreman-proxy stop && \  
service puppetmaster stop && \  
systemctl disable foreman-proxy && \  
systemctl disable puppetmaster  
  
# Install requierement for puppet env  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mercurial && \  
mkdir /root/.ssh  
  
# Install requierement for EFS  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nfs-common && \  
mkdir /install && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY files/install /install  
RUN chmod +x /install/entrypoint.sh && \  
chmod +x /install/scripts/* && \  
cp -rf /install/conf/openssl.cnf /etc/ssl/openssl.cnf  
  
COPY files/supervisord /etc/supervisor  
EXPOSE 8443  
EXPOSE 8140  
ENTRYPOINT ["/install/entrypoint.sh"]  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

