## Emacs, make this -*- mode: sh; -*-  
## start with the Docker 'base R' Debian-based image  
FROM rocker/r-base  
  
## This handle reaches Mario  
MAINTAINER "Mario Annau" mario.annau@gmail.com  
  
## LaTeX:  
## This installs inconsolata fonts used in R vignettes/manuals manually since
texlive-fonts-extra is HUGE  
RUN apt-get update \  
&& apt-get install -t unstable -y --no-install-recommends \  
aspell \  
aspell-en \  
ghostscript \  
imagemagick \  
lmodern \  
texlive-fonts-recommended \  
texlive-humanities \  
texlive-latex-extra \  
texinfo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& cd /usr/share/texlive/texmf-dist \  
&& wget http://mirrors.ctan.org/install/fonts/inconsolata.tds.zip \  
&& unzip inconsolata.tds.zip \  
&& rm inconsolata.tds.zip \  
&& echo "Map zi4.map" >> /usr/share/texlive/texmf-dist/web2c/updmap.cfg \  
&& mktexlsr \  
&& updmap-sys  
  
## Install further dependencies  
RUN apt-get update \  
&& apt-get install -t unstable -y --no-install-recommends \  
libssl-dev \  
libcurl4-openssl-dev \  
libxml2-dev \  
libhdf5-dev \  
libsqlite3-dev \  
sqlite3 \  
s3cmd  
  
RUN ln -s /usr/share/doc/littler/examples/check.r /usr/local/bin/check.r  
  
RUN Rscript -e "install.packages(c('testthat', 'RUnit', 'devtools'))"  

