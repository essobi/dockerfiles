#tianon/latex  
#FROM debian:latest  
FROM ubuntu:latest  
#FROM ubuntu:rolling  
ARG DEBIAN_FRONTEND=noninteractive  
RUN export LANG=C.UTF-8 &&\  
apt-get clean &&\  
apt-get update &&\  
apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
apt-get update &&\  
apt-get -y upgrade &&\  
apt-get -y dist-upgrade &&\  
# install utilities  
apt-get install -f -y apt-utils python-software-properties software-
properties-common&&\  
#add-apt-repository ppa:jonathonf/texlive -y &&\  
add-apt-repository ppa:jonathonf/texlive-2016 -y &&\  
apt-get update &&\  
# install some nice chinese fonts  
apt-get install -f -y fonts-arphic-bkai00mp \  
fonts-arphic-bsmi00lp \  
fonts-arphic-gbsn00lp \  
fonts-arphic-gkai00mp \  
fonts-arphic-ukai \  
fonts-arphic-uming \  
ttf-wqy-microhei \  
ttf-wqy-zenhei \  
xfonts-intl-chinese \  
xfonts-intl-chinese-big &&\  
apt-get install -f -y texlive-full biber latexmk make ghostscript latex-cjk-
common latex-cjk-chinese \  
texlive-fonts-extra texlive-fonts-recommended texlive-math-extra texlive-lang-
cjk \  
texlive-luatex texlive-pstricks texlive-science texlive-xetex \  
texlive-latex-extra texlive-lang-arabic xfonts-intl-arabic \  
xfonts-efont-unicode xfonts-efont-unicode-ib &&\  
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
# clean up all temporary files  
apt-get clean &&\  
apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
apt-get clean &&\  
rm -rf /tmp/* /var/tmp/* &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /etc/ssh/ssh_host_*  
  

