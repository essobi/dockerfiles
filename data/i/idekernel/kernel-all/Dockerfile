FROM idekernel/kernel-php:notebook  
USER root  
  
# R pre-requisites  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
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
libxrender1 \  
inkscape \  
fonts-dejavu \  
gfortran \  
gcc && apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
# R packages  
RUN conda config --add channels r && \  
conda install --quiet --yes \  
r-base \  
r-irkernel \  
r-plyr \  
r-devtools \  
r-tidyverse \  
r-shiny \  
r-rmarkdown \  
r-forecast \  
r-rsqlite \  
r-reshape2 \  
r-nycflights13 \  
r-caret \  
r-rcurl \  
r-crayon \  
r-randomforest && conda clean -tipsy  

