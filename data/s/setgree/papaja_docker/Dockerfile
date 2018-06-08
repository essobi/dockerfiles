FROM rocker/rstudio-stable:latest  
## Work-around to make Docker Hub use the Dockerfile  
## from https://github.com/rocker-org/rocker-versioned/tree/master/rstudio  
  
MAINTAINER Seth Green <seth@codeocean.com>  
  
# apt-get dependencies for papaja  
RUN apt-get update && apt-get install -y \  
texlive \  
texlive-publishers \  
texlive-fonts-extra \  
texlive-latex-extra \  
texlive-humanities \  
lmodern \  
zlib1g-dev \  
# necessary for git2r, which is a dependency of devtools  
libxml2-dev \  
libcairo2-dev \  
libssh2-1-dev \  
libudunits2-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
ed \  
&& rm -rf /var/lib/apt/lists/  
  
RUN R -e "install.packages('devtools',
dependencies=c('Depends','Imports','LinkingTo'));
devtools::install_github('crsh/papaja')"  
  
CMD ["/init"]  

