## start with the Docker 'R-devel' Debian-based image  
FROM rocker/drd:latest  
  
## maintainer  
MAINTAINER Seung Hoan Choi <schoi@broadinstitute.org>  
  
## Install GENESIS  
RUN apt-get update -qq \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y --no-install-recommends -t unstable \  
apt-utils \  
bwidget \  
curl \  
gdal-bin \  
git \  
gsl-bin \  
libgdal-dev \  
libgeos-dev \  
libgeos++-dev \  
libproj-dev \  
libspatialite-dev \  
libssl-dev \  
libv8-dev \  
libxml2-dev \  
netcdf-bin \  
pandoc pandoc-citeproc\  
qpdf \  
r-cran-rgl \  
r-cran-tkrplot \  
tcl8.6-dev \  
texinfo \  
texlive-base \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-recommended \  
tk8.6-dev \  
&& Rscript -e 'recommended <\-
unname(installed.packages(priority="recommended")[,"Package"]);
install.packages(recommended, lib=.Library, dependencies=TRUE)' \  
&& Rscript -e 'source("https://bioconductor.org/biocLite.R");
biocLite(pkgs=c("GENESIS","SeqVarTools","GWASTools"),lib=.Library,suppressUpdates=T)'
\  
&& install.r devtools \  
logistf \  
survey \  
CompQuadForm \  
RUnit \  
knitr \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& apt-get autoremove -qy \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/apt/lists  

