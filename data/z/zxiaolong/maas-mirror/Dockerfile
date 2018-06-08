FROM ubuntu:16.04  
  
RUN apt-get update && apt-get install -y simplestreams ubuntu-cloudimage-
keyring apache2 \  
&& sstream-mirror --keyring=/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
\  
http://maas.ubuntu.com/images/ephemeral-v2/daily/
/var/www/html/maas/images/ephemeral-v2/daily \  
'arch~(amd64|arm64)' 'subarch~(generic|hwe-x)' 'release~(trusty)' \--max=1
\--progress --verbose  
  

