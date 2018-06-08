FROM ubuntu:16.04  
  
MAINTAINER Jan Frederick Eick <jan-frederick.eick@uni-weimar.de>  
  
RUN apt-get update && apt-get install --yes \--no-install-recommends \  
openssh-client \  
make \  
git \  
curl \  
python3-setuptools \  
python3-pip \  
python3-pil \  
texlive \  
texlive-fonts-recommended \  
texlive-lang-german \  
texlive-lang-cyrillic \  
texlive-lang-english \  
texlive-latex-extra \  
texlive-latex-recommended \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install Sphinx sphinx_bootstrap_theme sphinx_rtd_theme alabaster
recommonmark javasphinx  
RUN mkdir /doc && chmod 755 /doc  
WORKDIR /doc  

