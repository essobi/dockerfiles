FROM eeacms/centos:7s  
MAINTAINER "Olimpiu Rob" <olimpiu.rob@eaudeweb.ro>  
  
ENV ZEO_HOME=/opt/zeoserver \  
ZEO_USERNAME=zope-www \  
ZEO_UID=500 \  
ZEO_GID=500  
# Setup gosu for easier command execution  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& rm -r /root/.gnupg/ \  
&& chmod +x /usr/local/bin/gosu \  
&& mkdir -p $ZEO_HOME  
  
COPY src/base.cfg src/bootstrap.py $ZEO_HOME/  
COPY docker-manage-permissions.sh docker-entrypoint.sh docker-initialize.py /  
  
WORKDIR $ZEO_HOME  
  
RUN python bootstrap.py -v 2.2.1 --setuptools-version=7.0 -c base.cfg && \  
./bin/buildout -c base.cfg && \  
groupadd -g $ZEO_GID $ZEO_USERNAME && \  
useradd -u $ZEO_UID -g $ZEO_GID -m -s /bin/bash $ZEO_USERNAME && \  
chown -R $ZEO_UID:$ZEO_GID $ZEO_HOME  
  
VOLUME $ZEO_HOME/var/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]  

