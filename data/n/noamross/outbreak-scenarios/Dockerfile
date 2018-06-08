# image: ecohealthalliance/outbreak-scenarios  
#  
# Provides environment required to build Rmd files.  
#  
# Use:  
# link the working directory of the site to build.  
# (`-e` keys only needed if using the twitter plugin)  
#  
# docker run --rm -v $(pwd):/data -w /data \  
# -e TWIT_KEY -e TWIT_SECRET -e TWIT_TOK - e TWIT_TOK_SECRET \  
# cboettig/labnotebook  
FROM rocker/hadleyverse  
MAINTAINER Noam Ross ross@ecohealthalliance.org  
  
## Install other software needed for builds  
#RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/archive/0.12.2.3.tar.gz \  
# && tar xf 0.12.2.3.tar.gz  
# RUN apt-get update && apt-get install -y wkhtmltopdf; exit 0  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz \  
&& tar xf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz \  
&& cp wkhtmltox/bin/wkhtmltopdf /usr/bin \  
&& cp wkhtmltox/bin/wkhtmltoimage /usr/bin \  
&& rm wkhtmltox-0.12.3_linux-generic-amd64.tar.xz \  
&& rm -r wkhtmltox  
  
RUN apt-get update && apt-get install fonts-lato  
  
# Set font rendering correctly  
RUN wget http://pastebin.com/raw.php?i=AmfYN3er -O
/etc/fonts/conf.d/10-wkhtmltopdf.conf  
  
RUN rm /usr/local/bin/pandoc && rm /usr/local/bin/pandoc-citeproc  
  
RUN wget
https://github.com/jgm/pandoc/releases/download/1.16.0.2/pandoc-1.16.0.2-1-amd64.deb
&& \  
dpkg -i pandoc* && \  
rm pandoc* && \  
apt-get clean  
  
# Allow non-free downloads  
RUN echo "deb http://gce_debian_mirror.storage.googleapis.com wheezy contrib
non-free" >> /etc/apt/sources.list \  
&& echo "deb http://gce_debian_mirror.storage.googleapis.com wheezy-updates
contrib non-free" >> /etc/apt/sources.list \  
&& echo "deb http://security.debian.org/ wheezy/updates contrib non-free" >>
/etc/apt/sources.list \  
&& apt-get update  
  
# This line accepts the Microsoft End User License Agreement allowing use of  
# the MS True Type core fonts  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install fonts-droid-fallback
msttcorefonts  
  
## Install all the R packages from Github  
RUN installGithub.r noamross/noamtools \  
# davidgohel/ReporteRsjars  
# davidgohel/ReporteRs  
noamross/readr \  
&& rm -rf /tmp/downloaded_packages  
  
## Install all the R packages from CRAN  
RUN install2.r -r http://cran.rstudio.com \  
knitr \  
ReporteRs \  
deSolve \  
rootSolve \  
# readr \  
# dplyr \  
# magrittr \  
# tidyr \  
# stringi \  
# lubridate \  
# ggplot2 \  
# broom \  
progress \  
cowplot \  
knitcitations \  
svglite \  
viridis \  
scales \  
# readxl \  
assertr \  
mclust \  
mgcv \  
binom \  
rmarkdown \  
import \  
arm \  
&& rm -rf /tmp/downloaded_packages  
  

