# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
  
FROM ritjupyter/base-notebook  
  
MAINTAINER Joshua Milas <jgm6496@rit.edu>  
  
USER root  
  
# Install all OS dependencies for fully functional notebook server  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
git \  
vim \  
jed \  
emacs \  
build-essential \  
python-dev \  
unzip \  
libsm6 \  
pandoc \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-xetex \  
lmodern \  
libxrender1 \  
inkscape \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install ipywidgets  
RUN conda install --quiet --yes \  
'ipywidgets=5.1*' && \  
conda clean -tipsy  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_USER  

