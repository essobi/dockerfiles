FROM rocker/r-base  
  
##########################################################  
# docker build -f Dockerfile.base -t vanessa/aim-ml:base .  
#  
# This is a base image for the aim-ml pipeline  
# container. The R dependencies take a while to  
# install, so we use this base to not need to install  
# each time  
##########################################################  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# zlib1g-dev is for git2r  
RUN apt-get update && apt-get install -y apt-utils \  
python3 \  
python3-pip \  
git \  
zlib1g-dev \  
libcurl4-openssl-dev \  
libssl-dev  
  
  
##############################################  
# Global Dependency Installation  
##############################################  
  
RUN Rscript -e "install.packages('callr')"  
RUN Rscript -e "install.packages('cli')"  
RUN Rscript -e "install.packages('digest')"  
RUN Rscript -e "install.packages('git2r')"  
RUN Rscript -e "install.packages('httr')"  
RUN Rscript -e "install.packages('jsonlite')"  
RUN Rscript -e "install.packages('memoise')"  
RUN Rscript -e "install.packages('rcmdcheck')"  
RUN Rscript -e "install.packages('rstudioapi')"  
RUN Rscript -e "install.packages('sessioninfo')"  
RUN Rscript -e "install.packages('usethis')"  
RUN Rscript -e "install.packages('whisker')"  
RUN Rscript -e "install.packages('withr')"  
RUN Rscript -e "install.packages('desc')"  
RUN Rscript -e "install.packages('rprojroot')"  
RUN Rscript -e "install.packages('knitr')"  
  
RUN git clone https://github.com/r-lib/pkgbuild.git && cd pkgbuild && R CMD
build . && R CMD INSTALL --build pkg*tar.gz  
RUN git clone https://github.com/r-lib/pkgload.git && cd pkgload && R CMD
build . && R CMD INSTALL --build pkg*tar.gz  
RUN git clone https://github.com/hadley/devtools.git && cd devtools && R CMD
build . && R CMD INSTALL --build devtools*.tar.gz  
  
ENV PATH /usr/local/bin:$PATH  

