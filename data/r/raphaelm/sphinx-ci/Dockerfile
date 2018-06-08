FROM debian:jessie  
  
MAINTAINER Raphael Michel  
USER root  
  
RUN apt-get update && apt-get install -y wget python3 git python3-pip \  
python3-sphinx python3-pil texlive-latex-extra texlive-fonts-recommended \  
texlive-latex-recommended texlive-latex-recommended dvipng locales \  
git curl build-essential python3-sphinxcontrib.httpdomain \  
\--no-install-recommends  
  
WORKDIR /  
  
RUN locale-gen  
RUN update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

