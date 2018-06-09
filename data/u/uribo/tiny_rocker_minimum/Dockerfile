FROM rocker/rstudio:latest  
MAINTAINER "Shinya Uryu" r.sh1nya.uryu@gmail.com  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
libxml2-dev \  
zlib1g-dev \  
emacs25  
  
# For knitr pdf output  
RUN apt-get install -y \  
texlive-latex-base \  
texlive-fonts-recommended \  
texlive-fonts-extra  
  
RUN apt-get install -y --no-install-recommends \  
r-base-dev  
  
RUN install2.r \  
rmarkdown tidyverse prettycode devtools \  
testthat remotes

