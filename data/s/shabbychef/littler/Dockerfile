#  
# rocker/r-base + littler  
#  
# VERSION 0.1  
#  
# docker build --rm -t shabbychef/littler .  
#  
# Created: 2015.10.01  
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
# update ubuntu, get the package, make some links, clean up  
ENV REPOS http://cran.rstudio.com  
  
# according to Dirk, rocker/r-base ships with littler, so no need to install
it?  
RUN (rm -rf /var/lib/apt/lists/* ; \  
apt-get clean -y ; \  
apt-get update -y -qq; \  
apt-get update --fix-missing ; \  
DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get
install -y --no-install-recommends -q \  
libxml2-dev libcurl4-gnutls-dev libssl-dev pkg-config libssh2-1-dev ; \  
apt-get clean -y ; \  
[ -f /usr/local/bin/install.r ] || ln -s /usr/lib/R/site-
library/littler/examples/install.r /usr/local/bin/install.r ; \  
[ -f /usr/local/bin/install2.r ] || ln -s /usr/lib/R/site-
library/littler/examples/install2.r /usr/local/bin/install2.r ; \  
[ -f /usr/local/bin/installGithub.r ] || ln -s /usr/lib/R/site-
library/littler/examples/installGithub.r /usr/local/bin/installGithub.r ; \  
/usr/local/bin/install.r docopt drat devtools )  
  
#####################################################  
# entry and cmd# FOLDUP  
# always use array syntax:  
ENTRYPOINT ["/usr/bin/r"]  
  
# ENTRYPOINT and CMD are better together:  
CMD ["-i","-"]  
# UNFOLD  
  
#for vim modeline: (do not edit)  
#
vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

