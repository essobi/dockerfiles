FROM benhutchins/mediawiki:1.25  
MAINTAINER Benjamin Hutchins <bhutchins@milcord.com>  
  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
libldb-dev \  
libaprutil1-dev \  
&& ln -fs /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install ldap  
  
COPY extensions/ /usr/src/mediawiki/extensions/  

