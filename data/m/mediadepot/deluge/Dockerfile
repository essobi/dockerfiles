FROM debian:jessie  
MAINTAINER jason@thesparktree.com  
  
#Create internal depot user (which will be mapped to external DEPOT_USER, with
the uid and gid values)  
RUN groupadd -g 15000 -r depot && useradd --uid 15000 -r -g depot depot  
  
#Install base applications + deps  
RUN apt-get -q update && \  
apt-get install -qy --force-yes python-cheetah deluged deluge-webui curl && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
#Create deluge folder structure & set as volumes  
RUN mkdir -p /srv/deluge/config && \  
mkdir -p /srv/deluge/data && \  
mkdir -p /srv/deluge/tmpl && \  
  
# create deluge storage structure  
mkdir -p /mnt/blackhole && \  
mkdir -p /mnt/processing && \  
mkdir -p /mnt/downloads  
  
  
#Copy over start script and docker-gen files  
ADD ./start.sh /srv/start.sh  
RUN chmod u+x /srv/start.sh  
ADD ./template/auth.tmpl /srv/deluge/tmpl/auth.tmpl  
ADD ./template/autoadd.tmpl /srv/deluge/tmpl/autoadd.tmpl  
ADD ./template/core.tmpl /srv/deluge/tmpl/core.tmpl  
ADD ./template/label.tmpl /srv/deluge/tmpl/label.tmpl  
ADD ./template/scheduler.tmpl /srv/deluge/tmpl/scheduler.tmpl  
ADD ./template/web.tmpl /srv/deluge/tmpl/web.tmpl  
  
VOLUME ["/srv/deluge/config", "/srv/deluge/data"]  
  
EXPOSE 8081  
CMD ["/srv/start.sh"]

