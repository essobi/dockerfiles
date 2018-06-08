# From pytorch compiled from source  
FROM rorydm/pytorch_extras:jupyter  
  
# pre-reqs for base notebooks from jupyter-stacks  
ENV export DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
wget \  
bzip2 \  
sudo \  
locales \  
tzdata \  
fonts-liberation  
  
# all OS dependencies for fully functional notebook server from jupyter-stacks  
RUN apt-get install -yq --no-install-recommends \  
emacs \  
inkscape \  
jed \  
libsm6 \  
libxext-dev \  
libxrender1 \  
lmodern \  
pandoc \  
python-dev \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-xetex \  
unzip  
  
# R pre-requisites from jupyter-stacks  
RUN apt-get install -yq --no-install-recommends \  
fonts-dejavu \  
gfortran \  
gcc  
  
# R packages  
RUN conda install -y -c r \  
r-base \  
r-irkernel \  
r-devtools \  
r-tidyverse \  
r-rmarkdown \  
r-glmnet \  
r-caret \  
r-gplots \  
r-rcolorbrewer && \  
conda clean -tipsy  
  
# R-python interface  
RUN conda install -y rpy2 && \  
conda clean -tipsy  
  
# bioconductor and packages  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R")' -e
'biocLite("splatter")'  

