## Start with the official rocker image (lightweight Debian)  
## Inspired by cardcorp/r-pandoc  
FROM rocker/r-base:latest  
  
MAINTAINER Mario Annau <mario.annau@gmail.com>  
  
## Install LaTeX  
## Source: https://registry.hub.docker.com/u/rocker/hadleyverse/dockerfile/  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ghostscript \  
imagemagick \  
lmodern \  
texlive-fonts-recommended \  
texlive-humanities \  
texlive-latex-extra \  
texinfo \  
texlive-base \  
texlive-binaries \  
texlive-fonts-extra \  
texlive-generic-recommended \  
texlive-humanities \  
texlive-latex-base \  
texlive-latex-recommended \  
texlive-pictures \  
pandoc  
  
## Install knitr other packages  
RUN install2.r --error \  
knitr \  
pander \  
rmarkdown \  
revealjs \  
tint \  
tufte \  
formatR \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  

