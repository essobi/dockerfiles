# Copyright (c) 2017 Arista Networks, Inc. All rights reserved.  
# Arista Networks, Inc. Confidential and Proprietary.  
FROM aristanetworks/base  
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"  
  
# Install nginx, certbot and kubectl  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& add-apt-repository ppa:certbot/certbot \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
nginx \  
certbot \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm /etc/nginx/sites-enabled/default \  
&& wget -nv https://storage.googleapis.com/kubernetes-
release/release/v1.8.1/bin/linux/amd64/kubectl \  
-O /usr/local/bin/kubectl \  
&& echo "e3e5d59be033ea6b46cfb65d6f8a0861e5c6322a /usr/local/bin/kubectl" |
sha1sum -c - \  
&& chmod +x /usr/local/bin/kubectl \  
&& mkdir -p /var/www/letsencrypt \  
&& chmod -R 755 /var/www/letsencrypt  

