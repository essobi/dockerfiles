# gollum in 32 bit  
#  
# VERSION 0.1  
#  
# this is just copied from suttang/gollum.  
# cf. https://github.com/suttang/docker-gollum  
#  
# however, the image there is 64 bit.  
# so remake to get 32 bit.  
#  
# cf. https://github.com/docker/docker/issues/7924  
#  
# to build  
#  
# docker build --rm -t shabbychef/gollum32 .  
#  
# run it as  
#  
# docker run -d -p 0.0.0.0:8080:4567 -v /my/wiki/dir:/srv/gollum:rw --name
gollum shabbychef/gollum32  
#  
# cf. http://msimav.net/2013/08/01/gollum-a-lightweight-wiki/  
#  
# no docker exec in 32 bit, so cannot exec in and touch _Sidebar.md  
#  
# cf. http://blackbe.lt/github-wiki-sidebar-table-contents-header-footer/  
#  
# Created: 2015.09.03  
# Copyright: Steven E. Pav, 2015  
# Author: Steven E. Pav  
# Comments: Steven E. Pav  
  
FROM 32bit/ubuntu:14.04  
  
MAINTAINER Steven E. Pav, shabbychef@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN (apt-get update ; \  
apt-get upgrade -y ; \  
apt-get install -y -q build-essential ruby1.9.3 python2.7 ruby-bundler libicu-
dev libreadline-dev libssl-dev zlib1g-dev git-core ; \  
apt-get clean ; \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* ; \  
gem install gollum redcarpet github-markdown ; \  
mkdir -p /srv/gollum ; \  
git init /srv/gollum )  
  
# Expose default gollum port 4567  
EXPOSE 4567  
  
# ENTRYPOINT and CMD are better together:  
ENTRYPOINT ["/usr/local/bin/gollum"]  
CMD ["--port","4567","--base-pat","wiki","--mathjax","--no-live-preview","--
user-icons","gravatar","--h1-title","/srv/gollum"]  
  
#for vim modeline: (do not edit)  
#
vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

