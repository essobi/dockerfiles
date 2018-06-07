FROM debian:stretch-slim  
  
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
sphinx_rtd_theme alabaster recommonmark guzzle_sphinx_theme  
RUN mkdir /doc && chmod 777 /doc  
WORKDIR /doc  

