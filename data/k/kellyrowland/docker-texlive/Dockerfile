#  
# Adapted from thomasweise/texlive  
# and from Kamshak/docker-texlive-biber  
#  
# This is an image with a basic TeX Live installation.  
# Source: https://github.com/thomasWeise/docker-texlive/  
# License: GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007  
# The license applies to the way the image is built, while the  
# software components inside the image are under the respective  
# licenses chosen by their respective copyright holders.  
#  
FROM ubuntu:16.04  
MAINTAINER Kelly Rowland <kellylynnerowland@gmail.com>  
  
RUN export LANG=C.UTF-8 &&\  
apt-get clean &&\  
apt-get update &&\  
apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
apt-get update &&\  
# install utilities  
apt-get install -f -y apt-utils &&\  
# install TeX Live  
apt-get install -f -y make=4.1* \  
texlive-full=2015.2016* \  
texlive-fonts-extra=2015.2016* \  
texlive-fonts-recommended=2015.2016* \  
texlive-math-extra=2015.2016* \  
texlive-pstricks=2015.2016* \  
texlive-science=2015.2016* &&\  
# install biber  
apt-get install -f -y biber &&\  
# install vim  
apt-get install -f -y vim &&\  
# install pdftk  
apt-get install -f -y pdftk &&\  
# free huge amount of unused space  
apt-get purge -f -y make-doc \  
texlive-fonts-extra-doc \  
texlive-fonts-recommended-doc \  
texlive-humanities-doc \  
texlive-latex-base-doc \  
texlive-latex-extra-doc \  
texlive-latex-recommended-doc \  
texlive-metapost-doc \  
texlive-pictures-doc \  
texlive-pstricks-doc \  
texlive-science-doc &&\  
# ensure that external fonts and doc folders exists  
mkdir /usr/share/fonts/external/ &&\  
mkdir /doc/ &&\  
# clean up all temporary files  
apt-get clean &&\  
apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
apt-get clean &&\  
rm -rf /tmp/* /var/tmp/* &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /etc/ssh/ssh_host_*  
  
VOLUME ["/doc/", "/usr/share/fonts/external/"]  
  
ADD scripts /bin/  
  
ENTRYPOINT ["/bin/__boot__.sh"]  

