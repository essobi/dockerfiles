#  
# dockerfile to use knitr/latex with r  
#  
# docker build --rm -t shabbychef/knitrer .  
#  
# docker run -it --rm --volume $(pwd):/srv:rw knitrer  
#  
# Created: 2018.05.11  
# Copyright: Steven E. Pav, 2018  
# Author: Steven E. Pav  
# Comments: Steven E. Pav  
  
#####################################################  
# preamble# FOLDUP  
FROM rocker/drd  
MAINTAINER Steven E. Pav, shabbychef@gmail.com  
USER root  
# UNFOLD  
  
ENV REPOS http://cran.rstudio.com  
  
# according to Dirk, rocker/r-base ships with littler, so no need to install
it?  
RUN (rm -rf /var/lib/apt/lists/* ; \  
apt-get clean -y ; \  
apt-get update -y -qq; \  
apt-get update --fix-missing ; \  
DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get
install -y --no-install-recommends -q \  
libxml2-dev libcurl4-gnutls-dev libssl-dev pkg-config libssh2-1-dev pandoc
ghostscript qpdf \  
libgs9 texlive-base texlive-binaries libcupsimage2 libcups2 curl wget \  
qpdf pandoc ghostscript texlive-latex-extra texlive-latex-base texlive-fonts-
recommended texlive-fonts-extra latexmk ; \  
sync ; \  
apt-get clean -y ; \  
[ -f /usr/local/bin/install.r ] || ln -s /usr/lib/R/site-
library/littler/examples/install.r /usr/local/bin/install.r ; \  
[ -f /usr/local/bin/install2.r ] || ln -s /usr/lib/R/site-
library/littler/examples/install2.r /usr/local/bin/install2.r ; \  
[ -f /usr/local/bin/installGithub.r ] || ln -s /usr/lib/R/site-
library/littler/examples/installGithub.r /usr/local/bin/installGithub.r ; \  
/usr/local/bin/install.r knitr docopt drat devtools )  
  
WORKDIR /srv  
  
#####################################################  
# entry and cmd# FOLDUP  
# always use array syntax:  
ENTRYPOINT ["R"]  
  
# ENTRYPOINT and CMD are better together:  
CMD ["--no-save"]  
# UNFOLD  
  
#for vim modeline: (do not edit)  
#
vim:et:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

