#  
# maker + onbuild directives.  
#  
# the ONBUILD directives first look for  
# ./apt_packages.txt, with a package on each line,  
# then attempts to apt-get install them.  
#  
# then it installs the Makefile  
#  
# VERSION 0.1  
#  
# docker build --rm -t shabbychef/maker-onbuild .  
#  
# Created: 2015.10.15  
# Copyright: Steven E. Pav, 2015  
# Author: Steven E. Pav  
# Comments: Steven E. Pav  
  
#####################################################  
# preamble# FOLDUP  
FROM shabbychef/maker  
MAINTAINER Steven E. Pav, shabbychef@gmail.com  
USER root  
# UNFOLD  
  
#####################################################  
# onbuild magic# FOLDUP  
ONBUILD COPY ./apt_packages.txt /tmp/apt_packages.txt  
ONBUILD RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true \  
[ -f /tmp/apt_packages.txt ] && grep -q -ve '^\s*#' /tmp/apt_packages.txt &&
apt-get update -y -q && apt-get install -y --no-install-recommends -q $(grep
-ve '^\s*#' /tmp/apt_packages.txt) || true;  
  
ONBUILD COPY ./Makefile /opt/make/Makefile  
# UNFOLD  
  
# everything else inherits from littler  
  
#for vim modeline: (do not edit)  
#
vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

