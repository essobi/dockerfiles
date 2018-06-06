FROM buildpack-deps:jessie-scm  
MAINTAINER crazycode  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# for install fonts wqy  
RUN echo "deb http://http.debian.net/debian wheezy-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y python-pip python-dev \  
texlive texlive-latex-recommended texlive-latex-extra texlive-fonts-
recommended texlive-xetex \  
fontconfig latex-cjk-chinese ttf-wqy-microhei ttf-wqy-zenhei && \  
apt-get -qq clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/bin/bash"]  

