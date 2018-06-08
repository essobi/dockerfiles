#  
# dockerfile to run vowpal wabbit  
#  
# docker build --rm -t shabbychef/vw .  
#  
# c.f.  
# https://hub.docker.com/r/bradleypallen/ml-dev/~/dockerfile/  
# https://github.com/JohnLangford/vowpal_wabbit#ubuntudebian-specific-info  
#  
# Created: 2016.02.22  
# Copyright: Steven E. Pav, 2016  
# Author: Steven E. Pav  
# Comments: Steven E. Pav  
  
#####################################################  
# preamble# FOLDUP  
FROM ubuntu:14.04  
MAINTAINER Steven E. Pav, shabbychef@gmail.com  
USER root  
# UNFOLD  
  
RUN (rm -rf /var/lib/apt/lists/* ; \  
apt-get clean -y ; \  
apt-get update -y -qq; \  
apt-get update --fix-missing ; \  
DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get
install -y --no-install-recommends -q \  
build-essential git libboost-program-options-dev zlib1g-dev ; \  
mkdir -p /tmp/build ; \  
cd /tmp/build ; \  
git clone git://github.com/JohnLangford/vowpal_wabbit.git ; \  
cd vowpal_wabbit; \  
make; \  
make test; \  
make install ; \  
apt-get clean -y ; )  
  
  
#####################################################  
  
# vw daemon listens to port 26542 by default.  
# so expose it on anticipation of daemon mode.  
# https://github.com/JohnLangford/vowpal_wabbit/wiki/Command-line-
arguments#input-options  
EXPOSE 26542  
  
# entry and cmd# FOLDUP  
# always use array syntax:  
ENTRYPOINT ["/usr/local/bin/vw"]  
  
# ENTRYPOINT and CMD are better together:  
CMD ['--help']  
# UNFOLD  
  
#for vim modeline: (do not edit)  
#
vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

