FROM ubuntu:xenial  
MAINTAINER Ivo Jimenez <ivo.jimenez@gmail.com>  
  
RUN apt-get -yq update && \  
apt-get install -qy --fix-missing \  
texlive-generic-extra texlive-fonts-extra \  
texlive texlive-latex-extra texlive-math-extra texlive-science \  
python-pygments texlive-xetex texlive-bibtex-extra make && \  
apt-get -yq autoremove && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

