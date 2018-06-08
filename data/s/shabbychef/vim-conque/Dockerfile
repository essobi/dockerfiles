#  
# try out vim-conque via docker  
#  
# VERSION 0.1  
#  
# docker build --rm -t shabbychef/vim-conque .  
#  
# Created: 2015.12.29  
# Copyright: Steven E. Pav, 2015  
# Author: Steven E. Pav  
# Comments: Steven E. Pav  
  
#####################################################  
# preamble# FOLDUP  
FROM rocker/r-base  
MAINTAINER Steven E. Pav, shabbychef@gmail.com  
USER root  
# UNFOLD  
  
#####################################################  
# update ubuntu, get packages, clean up.  
  
RUN (apt-get update -qq; \  
apt-get update --fix-missing ; \  
DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get
install -y --no-install-recommends -q vim vim-addon-manager vim-conque screen
r-base ; \  
vim-addons -w install conqueterm ; \  
apt-get -qq autoclean ; \  
apt-get -qq clean )  
  
COPY ./vimrc /root/.vimrc  
COPY ./screenrc /root/.screenrc  
COPY ./sample.R /tmp/sample.R  
  
VOLUME /tmp  
  
#####################################################  
# entry and cmd# FOLDUP  
# always use array syntax:  
ENTRYPOINT ["/usr/bin/vim"]  
  
# ENTRYPOINT and CMD are better together:  
CMD ["/tmp/sample.R"]  
# UNFOLD  
  
#for vim modeline: (do not edit)  
#
vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

