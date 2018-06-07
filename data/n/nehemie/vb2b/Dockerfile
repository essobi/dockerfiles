## Adapted from https://github.com/rocker-
org/rocker/blob/master/r-base/Dockerfile  
FROM debian:testing  
LABEL version="0.0.9000"  
  
MAINTAINER "Nehemie" nehemie.strupler@etu.unistra.fr  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
make \  
wget \  
locales  
  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
## install R, needed debian package and set a default CRAN repo  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
gdal-bin \  
liblwgeom-dev \  
libgdal-dev \  
libproj-dev \  
libgeos-dev \  
libudunits2-dev \  
r-base \  
r-base-dev \  
r-recommended \  
r-cran-backports \  
r-cran-data.table \  
r-cran-dplyr \  
r-cran-ggplot2 \  
r-cran-gtools \  
r-cran-hmisc \  
r-cran-htmlwidgets \  
r-cran-jsonlite \  
r-cran-latticeextra \  
r-cran-maptools \  
r-cran-knitr \  
r-cran-plyr \  
r-cran-raster \  
r-cran-reshape \  
r-cran-spatstat \  
r-cran-xtable \  
r-cran-zoo \  
&& echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site \  
&& Rscript -e "install.packages(c('rgdal', 'rgeos'))"  
# && Rscript -e "install.packages(c('foreign', 'dplyr', 'ggplot2', 'gtools',  
# 'knitr','plyr','raster', 'reshape', 'xtable'))" \  
# Install Inkscape and LaTeX  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
inkscape \  
texlive-base \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-xetex \  
biber \  
texlive-bibtex-extra \  
texlive-generic-extra \  
texlive-lang-french \  
texlive-lang-german \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-science  

