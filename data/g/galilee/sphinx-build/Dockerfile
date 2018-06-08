FROM debian:stretch  
LABEL maintainer="Stéphane BARON <sbaron@galilee.fr>"  
# Base install  
RUN apt-get update --yes \  
&& apt-get install --no-install-recommends --yes \--quiet \  
gcc \  
make \  
python \  
python-dev \  
python-pip \  
latexmk \  
texlive \  
texlive-lang-french \  
texlive-lang-english \  
texlive-latex-extra \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Modules install  
RUN pip install -U pip setuptools \  
&& pip install --upgrade sphinx sphinx_rtd_theme \  
&& rm -rf $HOME/.cache/pip

