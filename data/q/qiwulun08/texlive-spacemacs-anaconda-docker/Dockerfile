# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.19  
# 使用这个镜像的理由 http://lizorn.com/2016/11/02/docker-ubuntu-issue/  
MAINTAINER qiwulun08@gmail.com  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
# ...put your own build instructions here...  
RUN apt-get update  
# RUN add-apt-repository ppa:ubuntu-elisp/ppa  
# RUN apt-get update  
RUN apt-get install -y git make wget bzip2 ca-certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
mercurial subversion \  
build-essential openjdk-8-jre automake autoconf \  
libpng-dev libz-dev libpoppler-glib-dev libpoppler-private-dev \  
imagemagick  
  
# RUN apt-get install -y emacs-snapshot emacs-snapshot-el  
RUN apt-get install -y emacs pandoc silversearcher-ag bibtex2html figlet zeal
graphviz nikola  
RUN apt-get install -y xauth  
  
# anaconda  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
ENV PATH /opt/conda/bin:$PATH  
RUN conda install numpy scipy numba pillow h5py  
RUN pip install rx tqdm keras wakatime patterns flake8 minpy  
  
# texlive  
RUN export LANG=C.UTF-8 &&\  
apt-get clean &&\  
apt-get update &&\  
apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
apt-get update &&\  
# install utilities  
apt-get install -f -y apt-utils &&\  
# install some nice chinese fonts  
# apt-get install -f -y fonts-arphic-bkai00mp \  
# fonts-arphic-bsmi00lp \  
# fonts-arphic-gbsn00lp \  
# fonts-arphic-gkai00mp \  
# fonts-arphic-ukai \  
# fonts-arphic-uming \  
# ttf-wqy-microhei \  
# ttf-wqy-zenhei \  
# xfonts-intl-chinese \  
# xfonts-intl-chinese-big &&\  
# install TeX Live and ghostscript  
apt-get install -f -y ghostscript=9.18* \  
latex-cjk-common=4.8* \  
latex-cjk-chinese=4.8* \  
texlive-full=2015.2016* \  
texlive-fonts-extra=2015.2016* \  
texlive-fonts-recommended=2015.2016* \  
texlive-math-extra=2015.2016* \  
texlive-lang-cjk=2015.2016* \  
texlive-luatex=2015.2016* \  
texlive-pstricks=2015.2016* \  
texlive-science=2015.2016* \  
texlive-xetex=2015.2016* \  
asymptote \  
# for asymptote  
freeglut3 freeglut3-dev libreadline-gplv2-dev &&\  
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
  
RUN git clone https://github.com/syl20bnr/spacemacs.git /root/.emacs.d  
# RUN git clone https://github.com/syl20bnr/spacemacs.git /root/.emacs.d  
RUN cp /root/.emacs.d/core/templates/.spacemacs.template /root/.spacemacs  
RUN rm /root/.emacs.d/init.el  
COPY init.el /root/.emacs.d/init.el  
RUN emacs -batch -u root -kill  

