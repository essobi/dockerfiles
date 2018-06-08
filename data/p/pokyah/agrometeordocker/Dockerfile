# We build our custom image from the existing rocker/tidyverse image which is
an R install within an UBUNTU Linux.  
FROM rocker/tidyverse:latest  
  
# provide information about the maintainer of the image  
MAINTAINER Thomas Goossens (hello.pokyah@gmail.com)  
  
# Download and install hugo blog to work with R blogdown  
ENV HUGO_VERSION 0.22.1  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit.deb  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
/tmp/hugo.deb  
RUN dpkg -i /tmp/hugo.deb \  
&& rm /tmp/hugo.deb  
  
# We need to install all the UBUNTU dependencies required for our R-packages
to work properly  
RUN apt-get update && apt-get install -y \  
openssh-server \  
libxml2-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
libgeos-dev \  
libcairo2-dev \  
libudunits2-dev \  
gdal-bin \  
libgdal-dev \  
libproj-dev \  
freeglut3 \  
freeglut3-dev \  
mesa-common-dev \  
r-cran-rjava \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& install2.r --error \  
pacman \  
lubridate \  
anytime \  
jsonlite \  
here \  
nortest \  
lazyeval \  
maptools \  
rmarkdown \  
knitr \  
maps \  
broom \  
stringr \  
RPostgreSQL \  
chron \  
readr \  
plotly \  
ggpubr \  
BlandAltmanLeh \  
sf \  
raster \  
scales \  
mapview \  
citr \  
gstat \  
spData \  
shiny \  
blogdown \  
RColorBrewer \  
revealjs \  
rJava \  
RWekajars \  
mlr \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& rm -rf /var/lib/apt/lists/* \  
&& installGithub.r Nowosad/spDataLarge \  
&& rm -rf /tmp/downloaded_packages  
  
RUN R -e 'devtools::install_github("mlr-org/shinyMlr/package")'  
  
  
  
  
  
  

