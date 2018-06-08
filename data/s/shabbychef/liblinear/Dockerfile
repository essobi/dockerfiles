#  
# dockerfile to run (multicore) liblinear  
#  
# docker build --rm -t shabbychef/liblinear .  
#  
# test it:  
#  
# docker run -it --rm shabbychef/liblinear "-s" 3 "-n" "4"
"/tmp/build/liblinear-multicore-2.1-4/heart_scale"  
#  
# Created: 2016.03.08  
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
build-essential wget unzip ; \  
mkdir -p /tmp/build /opt/liblinear ; \  
cd /tmp/build ; \  
wget --no-check-certificate
https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/multicore-liblinear/liblinear-
multicore-2.1-4.zip ; \  
unzip liblinear-multicore-2.1-4.zip ; \  
cd liblinear-multicore-2.1-4 ; \  
make all ; \  
cp train predict /opt/liblinear/ ; \  
apt-get clean -y ; )  
  
#####################################################  
  
WORKDIR /opt/liblinear  
  
# entry and cmd# FOLDUP  
# always use array syntax:  
ENTRYPOINT ["/opt/liblinear/train"]  
  
# ENTRYPOINT and CMD are better together:  
CMD ['--help']  
# UNFOLD  
  
#for vim modeline: (do not edit)  
#
vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

