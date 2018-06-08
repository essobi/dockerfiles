# ----------------------------------------  
#  
# The primary intention of this image is to inherit  
# uoa-inzight-base image and install Lite specific  
# packages  
#  
# ----------------------------------------  
FROM scienceis/uoa-inzight-base:latest  
  
MAINTAINER "Science IS Team" ws@sit.auckland.ac.nz  
  
ENV BUILD_DATE "2018-05-06"  
# Install (via R) all of the necessary packages (R will automatially install
dependencies):  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 381BA480 \  
&& echo "deb http://deb.debian.org/debian stretch main" | sudo tee -a
/etc/apt/sources.list \  
&& apt-get update -y -q \  
  
&& apt-get install -y -q \  
default-jdk \  
libcurl4-openssl-dev \  
libv8-3.14-dev \  
libgdal-dev \  
libproj-dev \  
libprotobuf-dev \  
protobuf-compiler \  
libudunits2-dev \  
libgeos-dev \  
libpq-dev \  
libjq-dev \  
mesa-common-dev \  
libglu1-mesa-dev \  
gfortran \  
  
&& R -e "install.packages('RJSONIO', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('iNZightMR', repos =
'http://r.docker.stat.auckland.ac.nz/R/')" \  
&& R -e "install.packages(c('gridExtra', 'tidyr', 'dplyr', 'forcats'), repos =
'https://cran.r-project.org', type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('iNZightTS', repos =
'http://r.docker.stat.auckland.ac.nz/R/')" \  
&& R -e "install.packages('car', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE)" \  
  
&& R -e "install.packages('hextri', repos = 'https://cran.r-project.org', type
= 'source', dependencies = TRUE)" \  
&& R -e "install.packages('colorspace', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('RColorBrewer', repos =
'https://cran.r-project.org', type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('viridis', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('XML', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE)" \  
&& R -e "install.packages('gridSVG', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('RgoogleMaps', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('countrycode', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('foreign', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('sas7bdat', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('shinyjs', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('readxl', repos = 'https://cran.r-project.org', type
= 'source', dependencies = TRUE)" \  
  
&& apt-get install -y -q gcc-6 g++-6 \  
&& apt-get update -y -q \  
&& apt-get upgrade -y -q \  
&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave
/usr/bin/g++ g++ /usr/bin/g++-6 \  
  
&& R CMD javareconf \  
&& R -e "install.packages('GGally', repos = 'https://cran.r-project.org', type
= 'source', dependencies = TRUE)" \  
&& R -e "install.packages('gpairs', repos = 'https://cran.r-project.org', type
= 'source', dependencies = TRUE)" \  
&& R -e "install.packages('xlsx', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE)" \  
  
&& R -e "install.packages('iNZightRegression', repos =
'http://r.docker.stat.auckland.ac.nz/R/')" \  
  
&& R -e "install.packages('s20x', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE)" \  
&& R -e "install.packages('iNZightPlots', repos =
'http://r.docker.stat.auckland.ac.nz/R/')" \  
&& R -e "install.packages('iNZightMaps', repos =
'http://r.docker.stat.auckland.ac.nz/R/')" \  
  
&& R -e "install.packages('sf', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE)" \  
  
&& R -e "install.packages('devtools', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "devtools::install_github('tidyverse/ggplot2')" \  
  
&& rm -rf /tmp/* /var/tmp/*  
  

