# Forked from https://github.com/olavgg/moinmoin-wiki  
FROM debian:jessie  
MAINTAINER Clement Thomas <clement1289@hotmail.com>  
  
# Set the version you want of MoinMoin  
ENV MM_VERSION=1.9.8 MM_CSUM=4a616d12a03f51787ac996392f9279d0398bfb3b \  
MM_UID=1000 MM_ADMIN=mmAdmin MM_EMAIL=user@moinmoin.example.org \  
MM_VHOST=moinmoin.example.org  
  
# Install  
RUN apt-get update && apt-get install -qqy --no-install-recommends python curl
openssl nginx uwsgi uwsgi-plugin-python \  
&& curl -Ok
https://bitbucket.org/thomaswaldmann/moin-1.9/get/$MM_VERSION.tar.gz \  
&& if [ "$MM_CSUM" != "$(sha1sum $MM_VERSION.tar.gz | awk '{print($1)}')" ];
then exit 1; fi \  
&& mkdir moinmoin && tar xf $MM_VERSION.tar.gz -C moinmoin --strip-
components=1 && cd moinmoin \  
&& python setup.py install --force --prefix=/usr/local && mkdir -p
/usr/local/share/moin/underlay/pages  
  
ADD wikiconfig.py /usr/local/share/moin/  
ADD nginx.conf /etc/nginx/  
ADD moinmoin.conf /etc/nginx/sites-available/  
ADD run /opt/  
  
RUN chmod +x /opt/run && mkdir -p /var/cache/nginx/cache \  
&& ln -s /etc/nginx/sites-available/moinmoin.conf /etc/nginx/sites-
enabled/moinmoin.conf \  
&& rm /etc/nginx/sites-enabled/default && rm $MM_VERSION.tar.gz && rm -rf
/moinmoin && rm /usr/local/share/moin/underlay.tar && apt-get purge -qqy curl
\  
&& apt-get autoremove -qqy && apt-get clean && rm -rf /tmp/*
/var/lib/apt/lists/*  
  
EXPOSE 80  
ENTRYPOINT ["/opt/run"]  

