FROM mediadepot/base:python  
  
#Create headphones folder structure & set as volumes  
RUN mkdir -p /srv/plexpy/app && \  
mkdir -p /srv/plexpy/config && \  
mkdir -p /srv/plexpy/data/logs && \  
mkdir -p /srv/plexpy/data/cache  
  
WORKDIR /srv/plexpy/app  
  
#start.sh will download the latest version of headphones and run it.  
ADD ./start.sh /srv/start.sh  
RUN chmod u+x /srv/start.sh  
#  
VOLUME ["/srv/plexpy/config", "/srv/plexpy/data"]  
  
EXPOSE 8181  
CMD ["/srv/start.sh"]

