FROM flxel/base:latest  
MAINTAINER elseym <elseym@me.com>  
  
# configure  
EXPOSE 8181  
ENV FLXEL_SERVICE_CMD python /opt/plexpy/PlexPy.py --nolaunch --config
/config/plexpy/plexpy.conf --datadir /config/plexpy/data  
  
# install software  
RUN git clone https://github.com/drzoidberg33/plexpy.git /opt/plexpy  

