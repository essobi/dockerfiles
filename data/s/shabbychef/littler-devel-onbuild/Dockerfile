#  
# littler w/ r-devel + onbuild directives.  
#  
# the ONBUILD directives first look for  
# ./apt_packages.txt, with a package on each line,  
# then attempts to apt-get install them.  
# Lines in apt_packages.txt starting with '#' are comments, and are ignored.  
#  
# then looks for ./r_packages.txt, with an R package on each line,  
# then attempts to rinstall2 them.  
# Lines in r_packages.txt starting with '#' are comments, and are ignored.  
#  
# then looks for ./r_github_packages.txt, with an install_github package
description  
# on each line, then attempts to installGithub them. These should have the
form  
# 'username/repo[/subdir][@ref|#pull]'  
# Lines in r_github_packages.txt starting with '#' are comments, and are
ignored.  
#  
# VERSION 0.1  
#  
# docker build --rm -t shabbychef/littler-devel-onbuild .  
#  
# Created: 2015.12.16  
# Copyright: Steven E. Pav, 2015  
# Author: Steven E. Pav  
# Comments: Steven E. Pav  
  
#####################################################  
# preamble# FOLDUP  
FROM rocker/r-devel  
MAINTAINER Steven E. Pav, shabbychef@gmail.com  
USER root  
# UNFOLD  
  
# just make sure it is fresh:  
  
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
# onbuild magic# FOLDUP  
# c.f.  
# http://docs.docker.com/engine/articles/dockerfile_best-practices/#build-
cache  
ONBUILD COPY ./*_packages.txt /tmp/  
  
ONBUILD RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true \  
[ -f /tmp/apt_packages.txt ] && grep -q -ve '^\s*#' /tmp/apt_packages.txt &&
apt-get update -y -q && apt-get install -y --no-install-recommends -q $(grep
-ve '^\s*#' /tmp/apt_packages.txt) || true;  
  
ONBUILD RUN [ -f /tmp/r_packages.txt ] && grep -q -ve '^\s*#'
/tmp/r_packages.txt && /usr/local/bin/install.r $(grep -ve '^\s*#'
/tmp/r_packages.txt) || true;  
  
ONBUILD RUN [ -f /tmp/r_github_packages.txt ] && grep -q -ve '^\s*#'
/tmp/r_github_packages.txt && /usr/local/bin/installGithub.r $(grep -ve
'^\s*#' /tmp/r_github_packages.txt) || true;  
# UNFOLD  
  
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

