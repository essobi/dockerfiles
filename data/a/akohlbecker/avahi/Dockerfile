FROM akohlbecker/base:latest  
  
# Fixed uids/gids  
RUN groupadd --gid 125 --system avahi && \  
useradd --home-dir "/var/run/avahi-daemon" \--shell "/bin/false" \--comment
"Avahi mDNS daemon,,," \--uid 125 --system --gid 125 avahi  
  
RUN set -x && \  
apt-get --quiet --yes update && \  
apt-get --quiet --yes install avahi-daemon avahi-utils && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
USER root  
  
ADD avahi-daemon.conf /etc/avahi  
ADD services /etc/avahi/services  
  
CMD ["avahi-daemon"]  

