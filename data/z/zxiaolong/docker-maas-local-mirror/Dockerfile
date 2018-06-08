FROM ubuntu:16.04  
# IF you have downloaded maas image at /var/www/html/maas  
# Package to maas.tgz as a cache  
#ADD maas.tgz /var/www/html  
# apt cache on 10.197.0.68  
#RUN sed -i s/archive.ubuntu.com/10.197.0.68/g /etc/apt/sources.list && sed -i
s/security.ubuntu.com/10.197.0.68/g /etc/apt/sources.list  
RUN apt-get update && apt-get install -y simplestreams ubuntu-cloudimage-
keyring apache2 \  
&& sstream-mirror --keyring=/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
\  
http://maas.ubuntu.com/images/ephemeral-v2/daily/
/var/www/html/maas/images/ephemeral-v2/daily \  
'arch~(arm64)' 'subarch~(generic|hwe-x)' 'release~(trusty)' \--max=1
\--progress --verbose  
  

