FROM debian:jessie  
MAINTAINER Jeffrey Boehm "jeff@ressourcenkonflikt.de"  
  
ENV EGGDROP_HOME="/home/eggdrop/eggdrop"  
WORKDIR $EGGDROP_HOME  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
mysqltcl \  
eggdrop && \  
useradd eggdrop && \  
mkdir logs data && \  
chown -R eggdrop .  
  
VOLUME ["$EGGDROP_HOME/logs", "$EGGDROP_HOME/data"]  
  
USER eggdrop  
RUN zcat /usr/share/doc/eggdrop-data/examples/eggdrop.conf.gz > eggdrop.conf  
  
ENTRYPOINT ["eggdrop", "-n"]  

