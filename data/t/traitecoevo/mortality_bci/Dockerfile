FROM rocker/verse:3.4.1  
LABEL maintainer="James Camac"  
LABEL email="james.camac@gmail.com"  
  
# Install latex, git and clang then clean up tmp files  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
clang \  
zip \  
unzip \  
gdal-bin \  
libudunits2-dev \  
libgdal-dev \  
libproj-dev \  
python-dev \  
python-gdal \  
python-numpy  
  
# Global site-wide config  
RUN mkdir -p $HOME/.R/ \  
&& echo "\nCXXFLAGS=-O3 -mtune=native -march=native -Wno-unused-variable -Wno-
unused-function\n" >> $HOME/.R/Makevars \  
&& echo "\nCXX=clang++ -ftemplate-depth-256\n" >> $HOME/.R/Makevars \  
&& echo "CC=clang\n" >> $HOME/.R/Makevars  
  
# Install other dependent R packages (installed in batches to overcome
dependency issues)  
RUN . /etc/environment \  
&& install2.r --error --repos $MRAN \--deps TRUE \  
R6 yaml digest crayon getopt optparse downloader raster Hmisc rstan pbmcapply  
  
RUN . /etc/environment \  
&& install2.r --error --repos $MRAN \--deps FALSE \  
cowplot gridBase png  
  
# Install remake  
RUN installGithub.r \  
\--deps "TRUE" \  
richfitz/storr \  
richfitz/remake  
  
# Remove unnecesarry tmp files  
RUN rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
# Set working directory  
WORKDIR /home/mortality_bci/

