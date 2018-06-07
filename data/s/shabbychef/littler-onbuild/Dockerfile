#  
# littler + onbuild directives.  
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
# docker build --rm -t shabbychef/littler-onbuild .  
#  
# Created: 2015.10.01  
# Copyright: Steven E. Pav, 2015  
# Author: Steven E. Pav  
# Comments: Steven E. Pav  
  
#####################################################  
# preamble# FOLDUP  
FROM shabbychef/littler  
MAINTAINER Steven E. Pav, shabbychef@gmail.com  
USER root  
# UNFOLD  
  
# just make sure it is fresh:  
RUN rm -rf /var/lib/apt/lists/* && apt-get clean -y && apt-get update -y -q;  
  
#####################################################  
# onbuild magic# FOLDUP  
# c.f.  
# http://docs.docker.com/engine/articles/dockerfile_best-practices/#build-
cache  
ONBUILD COPY ./*_packages.txt /tmp/  
  
ONBUILD RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true \  
[ -f /tmp/apt_packages.txt ] && grep -q -ve '^\s*#' /tmp/apt_packages.txt && \  
apt-get update -y -qq && apt-get install -y --no-install-recommends -q $(grep
-ve '^\s*#' /tmp/apt_packages.txt) || true;  
  
ONBUILD RUN [ -f /tmp/r_packages.txt ] && grep -q -ve '^\s*#'
/tmp/r_packages.txt && \  
/usr/local/bin/install.r $(grep -ve '^\s*#' /tmp/r_packages.txt) || true;  
  
ONBUILD RUN [ -f /tmp/r_github_packages.txt ] && grep -q -ve '^\s*#'
/tmp/r_github_packages.txt && \  
/usr/local/bin/installGithub.r $(grep -ve '^\s*#' /tmp/r_github_packages.txt)
|| true;  
# UNFOLD  
  
# everything else inherits from littler  
  
#for vim modeline: (do not edit)  
#
vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

