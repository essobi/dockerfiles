FROM ubuntu:17.10  
MAINTAINER Ulrich Schreiner <ulrich.schreiner@gmail.com>  
  
RUN apt-get update && apt-get install --yes \--no-install-recommends \  
curl \  
git \  
make \  
python-pip \  
python-setuptools \  
texlive \  
texlive-fonts-recommended \  
texlive-lang* \  
texlive-latex-extra \  
texlive-latex-recommended \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install wheel && pip install Sphinx sphinx_bootstrap_theme
sphinx_rtd_theme alabaster recommonmark  
RUN mkdir /doc && chmod 777 /doc  
WORKDIR /doc  
  

