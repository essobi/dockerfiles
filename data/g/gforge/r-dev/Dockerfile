FROM rocker/r-devel  
MAINTAINER "Max Gordon" max@gforge.se  
  
## Remain current  
RUN apt-get update \  
&& apt-get upgrade -y  
  
RUN apt-get update  
  
RUN apt-get install -y \  
bash-completion \  
bison \  
debhelper \  
default-jdk \  
g++ \  
gcc \  
gdb \  
gfortran \  
groff-base \  
libbz2-dev \  
libcairo2-dev \  
libcurl4-openssl-dev \  
libjpeg-dev \  
liblapack-dev \  
liblzma-dev \  
libncurses5-dev \  
libpango1.0-dev \  
libpcre3-dev \  
libpng-dev \  
libreadline-dev \  
libtiff5-dev \  
libx11-dev \  
libxt-dev \  
mpack \  
subversion \  
tcl8.6-dev \  
icedtea-netx \  
libcairo2-dev \  
libgsl0-dev \  
libgdal-dev \  
libgeos-dev \  
libssl-dev \  
libpq-dev \  
libsqlite3-0 \  
libsqlite3-dev \  
libv8-dev \  
libxcb1-dev \  
libxdmcp-dev \  
libxml2-dev \  
libxslt1-dev \  
libxt-dev \  
netcdf-bin \  
qpdf \  
libicu-dev \  
ssh \  
pandoc \  
pandoc-citeproc \  
nano \  
libblas-dev \  
texinfo \  
texlive \  
texlive-fonts-extra \  
libmagick++-dev  
  
# Remove all regular package version  
RUN rm -rf /usr/local/lib/R/site-library/*  
RUN rm -rf /usr/lib/R/library/*  
  
RUN apt-get remove -y libdrm2  
RUN apt-get install -y libglu1-mesa-dev freeglut3-dev mesa-common-dev libdrm-
dev  
  
RUN /usr/local/bin/RDscript \  
-e "install.packages(c('knitr'), dependencies=TRUE)"  
  
RUN /usr/local/bin/RDscript \  
-e "install.packages(c('htmlTable', 'Gmisc', 'forestplot'), dependencies=TRUE)"  
  
RUN /usr/local/bin/RDscript \  
-e "install.packages(c('Greg'), dependencies=TRUE)"  
  
  
COPY resources /root  
WORKDIR "/root"  
  
RUN echo "./check_pkg.sh" > .bash_history  
  
CMD ["/bin/bash"]  

