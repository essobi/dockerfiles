FROM studioetrange/docker-debian:wheezy  
MAINTAINER StudioEtrange <nomorgan@gmail.com>  
  
  
# DEBIAN packages : SICKRAGE dependencies install ----------  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# NODEJS install ----------  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
  
# SUBNODE install -------------  
ENV ITEM_VERSION 1.1.15  
WORKDIR /data/subnode  
RUN ln -s /opt/subnode/appParams.json /data/subnode/appParams.json  
  
WORKDIR /opt/subnode  
RUN curl -k -SL
"https://github.com/ocombe/subNode/archive/$ITEM_VERSION.tar.gz" \  
| tar -xzf - -C /opt/subnode --strip-components=1  
  
RUN npm install --production --unsafe-perm  
  
# SUPERVISOR -------------  
COPY supervisord-subnode.conf /etc/supervisor/conf.d/supervisord-subnode.conf  
  
# DOCKER -------------  
VOLUME /data  
  
# Supervisord web interface -------  
EXPOSE 9999  
# subnode http port  
EXPOSE 3000  
# run command by default  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  

