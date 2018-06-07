#  
# my mini base image  
#  
#  
  
FROM gliderlabs/alpine:edge  
  
MAINTAINER Gunnar Falk <docker@grundstil.de>  
# inspired by https://github.com/colstrom/docker-alpine  
## Taken directly form https://github.com/colstrom/docker-alpine:  
# This includes the main, testing, and community repositories,  
# but all packages outside main are masked.  
# To import them, just use apk add package@tag.  
##  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/main | tee
/etc/apk/repositories \  
&& echo @testing http://nl.alpinelinux.org/alpine/edge/testing | tee -a
/etc/apk/repositories \  
&& echo @community http://nl.alpinelinux.org/alpine/edge/community | tee -a
/etc/apk/repositories \  
&& apk add --update \  
curl \  
wget \  
bash \  
tree \  
sed \  
rsync \  
openssh \  
vim \  
nano \  
ca-certificates \  
sudo \  
screen \  
busybox-suid \  
&& rm -rf /var/cache/apk/*  
  

