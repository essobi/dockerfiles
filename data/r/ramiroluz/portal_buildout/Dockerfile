FROM ubuntu:14.04  
ADD VERSION .  
  
RUN useradd --system --shell /bin/bash --comment 'Plone Administrator' \  
\--user-group -m --home-dir /opt/plone plone \  
&& mkdir -p /opt/plone /data/filestorage /data/blobstorage \  
&& chown -R plone:plone /opt/plone /data  
  
LABEL plone.version=4.3.9  
LABEL os="ubuntu" os.version="14.04"  
  
RUN buildDeps="curl sudo python-setuptools python-dev build-essential libssl-
dev libxml2-dev libxslt1-dev libbz2-dev libjpeg62-dev zlib1g-dev python-
imaging wv poppler-utils git ca-certificates" \  
&& runDeps="libxml2 libxslt1.1 libjpeg62 rsync" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& chown -R plone:plone /opt/plone /data \  
&& sudo -u plone git clone https://github.com/plonegovbr/portal.buildout.git
/opt/plone/portal.buildout \  
&& chown -R plone:plone /opt/plone /data \  
&& cd /opt/plone/portal.buildout \  
&& apt-get install -y --no-install-recommends $runDeps \  
&& sudo -u plone git checkout tags/1.1.5.2  
  
COPY base.cfg /opt/plone/portal.buildout/buildout.d/base.cfg  
COPY buildout.cfg /opt/plone/portal.buildout/buildout.cfg  
  
RUN sudo -u plone python /opt/plone/portal.buildout/bootstrap.py -c
/opt/plone/portal.buildout/buildout.cfg \  
&& sudo -u plone python /opt/plone/portal.buildout/bin/buildout -c
/opt/plone/portal.buildout/buildout.cfg \  
&& sed -i 's/^nodaemon = false$/nodaemon = true/'
/opt/plone/portal.buildout/parts/supervisor/supervisord.conf  
  
EXPOSE 8000  
USER plone  
WORKDIR /opt/plone/portal.buildout  
  
ENTRYPOINT ["/opt/plone/portal.buildout/bin/supervisord"]  

