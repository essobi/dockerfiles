# gitit  
#  
# VERSION 0.1  
#  
# docker build --rm -t shabbychef/gitit .  
#  
# Created: 2015.12.04  
# Copyright: Steven E. Pav, 2015  
# Author: Steven E. Pav  
# Comments: Steven E. Pav  
FROM haskell:7.10.2  
MAINTAINER Steven E. Pav, shabbychef@gmail.com  
  
RUN (cabal update ; \  
cabal install pandoc -fhighlighting --reinstall ; \  
cabal install gitit ; \  
ln -s /root/.cabal/bin/gitit /usr/local/bin/gitit ; \  
gitit --version ; \  
apt-get update -qq; \  
apt-get update -qq --fix-missing ; \  
DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get
install -y --no-install-recommends -q locales mime-support git openssh-client;
\  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 ;
\  
apt-get clean -y )  
  
# you will want to do  
# git config --global user.email "my@ema.il"  
# git config --global user.name "My Name"  
VOLUME ['/srv/gitit']  
  
WORKDIR /srv/gitit  
  
EXPOSE 5001  
# always use array syntax:  
ENTRYPOINT ["gitit"]  
  
# ENTRYPOINT and CMD are better together:  
CMD ['--port=5001','--config-file=/srv/gitit/gitit.conf']  
  
#for vim modeline: (do not edit)  
#
vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

