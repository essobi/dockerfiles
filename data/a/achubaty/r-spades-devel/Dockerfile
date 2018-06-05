## Emacs, make this -*- mode: sh; -*-  
## start with the Docker 'r-spatial-devel' Debian-based image  
FROM achubaty/r-spatial-devel:latest  
  
## maintainer of this script  
MAINTAINER Alex Chubaty <alex.chubaty@gmail.com>  
  
## 1. Remain current;  
## 2. get the current `SpaDES` package build for testing;  
## 3. Install `SpaDES` package dependencies;  
## 4. Cleanup downloaded packages.  
##  
## All of this is run in a single RUN command to get a single AUFS layer  
RUN apt-get update -qq \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y --no-install-recommends -t unstable \  
tcl8.6-dev \  
texinfo \  
texlive-base \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-recommended \  
tk8.6-dev \  
&& git clone --branch=development --single-branch --depth=1
https://github.com/PredictiveEcology/SpaDES.git \  
&& install.r R6 roxygen2 \  
&& xvfb-run -a RDscript -e 'tryCatch({ deps <\-
withr::with_libpaths(.Library.site[1], devtools::install_deps("SpaDES",
dependencies = TRUE)) }, error = function(e) { message(e); q(status=1) }); if
(!all(deps %in% installed.packages())) { message("missing: ",
paste(setdiff(deps, installed.packages()), collapse=", ")); q(status = 1, save
= "no") }' \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \\\  
&& dpkg --purge \  
tcl8.6-dev \  
tk8.6-dev \  
&& apt-get autoremove -qy \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/apt/lists  

