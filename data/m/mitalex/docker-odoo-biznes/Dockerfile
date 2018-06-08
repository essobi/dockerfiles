FROM odoo:latest  
MAINTAINER Mitalex s.r.o. <info@mitalex.org>  
  
USER root  
  
RUN set -x; apt-get update \  
&& apt-get install -y build-essential libssl-dev libffi-dev python-dev python-
openssl python-shapely python-geoip python-openssl python-geopy ; \  
for i in pip cffi simplejson pysftp inflect gengo geojson ; do pip install
--upgrade $i ; done ; \  
cd /tmp ; \  
curl -o maw.diff
https://github.com/odoo/odoo/commit/b9af10ebe47240bac23cdc6394075dda4d9836ae.diff
; \  
cd /usr/lib/python2.7/dist-packages/odoo ; \  
patch -p2 < /tmp/maw.diff  
  
USER odoo  
  

