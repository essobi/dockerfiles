#  
# dockerfile to CRAN-check with r-dev  
#  
# docker build --rm -t shabbychef/crancheck .  
#  
# docker run -it --rm --volume $(pwd):/srv:rw crancheck  
#  
# Created: 2016.01.10  
# Copyright: Steven E. Pav, 2016  
# Author: Steven E. Pav  
# Comments: Steven E. Pav  
  
#####################################################  
# preamble# FOLDUP  
#FROM rocker/r-devel  
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
ghostscript qpdf ; \  
apt-get clean -y ; \  
[ -f /usr/local/bin/install.r ] || ln -s /usr/lib/R/site-
library/littler/examples/install.r /usr/local/bin/install.r ; \  
[ -f /usr/local/bin/install2.r ] || ln -s /usr/lib/R/site-
library/littler/examples/install2.r /usr/local/bin/install2.r ; \  
[ -f /usr/local/bin/installGithub.r ] || ln -s /usr/lib/R/site-
library/littler/examples/installGithub.r /usr/local/bin/installGithub.r ; \  
/usr/local/bin/install.r docopt drat devtools )  
  
WORKDIR /srv  
  
# probably redundant, but see http://stackoverflow.com/a/10017736/164611  
ENV _R_CHECK_CRAN_INCOMING_ TRUE  
ENV _R_CHECK_FORCE_SUGGESTS_ FALSE  
ENV _R_CHECK_VC_DIRS_ TRUE  
ENV _R_CHECK_UNSAFE_CALLS_ TRUE  
ENV _R_CHECK_TIMINGS_ 10  
ENV _R_CHECK_INSTALL_DEPENDS_ TRUE  
ENV _R_CHECK_SUGGESTS_ONLY_ TRUE  
ENV _R_CHECK_NO_RECOMMENDED_ TRUE  
ENV _R_CHECK_SUBDIRS_NOCASE_ TRUE  
ENV _R_CHECK_EXECUTABLES_EXCLUSIONS_ FALSE  
ENV _R_CHECK_LICENSE_ TRUE  
ENV _R_CHECK_DOC_SIZES2_ TRUE  
ENV _R_CHECK_CODETOOLS_PROFILE_ 'suppressPartialMatchArgs=false'  
ENV _R_CHECK_VIGNETTES_NLINES_ 50  
ENV _R_CHECK_DOT_INTERNAL_ TRUE  
  
#####################################################  
# entry and cmd# FOLDUP  
# always use array syntax:  
ENTRYPOINT ["/usr/local/bin/Rdevel","CMD","check","--as-cran","--output=/tmp"]  
  
# ENTRYPOINT and CMD are better together:  
CMD ["/srv/*.tar.gz"]  
# UNFOLD  
  
#for vim modeline: (do not edit)  
#
vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql  

