# Copyright (c) Jupyter Development Team.  
# This is a fork of the notebooks from Jupyter Dev Team.  
# Distributed under the terms of the Modified BSD License.  
  
FROM marcsaric/base-notebook  
  
LABEL maintainer="Marc Saric <marc.saric@gmx.de>"  
  
USER root  
  
# Install all OS dependencies for fully functional notebook server  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
aptitude \  
build-essential \  
emacs \  
git \  
git-annex \  
htop \  
inkscape \  
jed \  
less \  
libcurl4-openssl-dev \  
libsm6 \  
libssl-dev \  
libxext-dev \  
libxrender1 \  
libxml2-dev \  
lmodern \  
man \  
netcat \  
pandoc \  
python-dev \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-xetex \  
unzip \  
vim \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_UID  

