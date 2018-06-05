FROM abstracttechnology/webapp  
MAINTAINER Giorgio Borelli <giorgio.borelli@abstract.it>  
  
  
# Install Plone dependencies  
RUN apt-get update && \  
apt-get install -y libpng12-dev libpng++-dev \  
gettext libreadline6-dev libbz2-dev libssl-dev libevent-dev \  
libsasl2-dev libpcre3-dev libxslt1-dev libxml2 \  
wv poppler-utils xpdf lynx npm && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install needed files  
COPY buildout.cfg buildout.cfg  
COPY base.cfg base.cfg  
COPY bootstrap.py bootstrap.py  
  
RUN python bootstrap.py \  
&& bin/buildout -v \  
&& chown -R webapp:webapp .  
  
VOLUME ["/srv/webapp/var/filestorage", "/srv/webapp/var/blobstorage",
"/srv/webapp/var/log"]  
  
USER webapp  
  
# Expose  
EXPOSE 8080  
CMD ["/srv/webapp/bin/instance","console"]  

