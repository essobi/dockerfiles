FROM ubuntu:14.04  
MAINTAINER "Cole Brokamp" cole.brokamp@gmail.com  
  
## ON BUILD  
ONBUILD RUN mkdir /srv/shiny-server/app  
ONBUILD COPY . /srv/shiny-server/app  
  
# copy config file if it exists  
ONBUILD RUN if [ -f /srv/shiny-server/app/shiny-server.conf ]; then (>&2 echo
"Using config file inside app directory") && cp /srv/shiny-server/app/shiny-
server.conf /etc/shiny-server/shiny-server.conf; fi  
  
# if it doesn't exist, download and copy the example config file  
ONBUILD RUN if [ ! -f /srv/shiny-server/app/shiny-server.conf ]; then (>&2
echo "Config file inside app directory not found; downloading example config
file") && wget https://raw.githubusercontent.com/cole-
brokamp/shiny_docker/master/example_shiny-server.conf -q -O /etc/shiny-
server/shiny-server.conf; fi  
  
# install necessary R packages  
ONBUILD RUN sudo su - -c "R -e \"setwd('/srv/shiny-server/app');
automagic::automagic()\""  
  
# start it  
ONBUILD CMD exec shiny-server >> /var/log/shiny-server.log 2>&1  
  
# set user  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker \  
&& addgroup docker staff  
  
RUN apt-get update && apt-get install -y \  
gdebi-core \  
pandoc pandoc-citeproc \  
libproj-dev libgdal-dev \  
libxml2-dev libxt-dev libcairo2-dev \  
libssh2-1-dev libcurl4-openssl-dev \  
less git make wget nano \  
software-properties-common python-software-properties \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install R  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install r-base-core -y --force-yes \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# set default CRAN repo and DL method  
RUN echo 'options(repos=c(CRAN = "https://cran.rstudio.com/"),
download.file.method="libcurl")' >> /etc/R/Rprofile.site  
  
# install R packages  
RUN sudo su - -c "R -e
\"install.packages(c('ghit','shiny','rmarkdown','tidyverse','rgeos','rgdal'))\""  
RUN sudo su - -c "R -e \"ghit::install_github('cole-brokamp/automagic')\""  
RUN sudo su - -c "R -e \"ghit::install_github('cole-brokamp/CB')\""  
  
# Download and install latest version of shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb && \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
# expose port to access app  
EXPOSE 3838  
# give docker user permission to write to logs  
RUN chown docker /var/log/shiny-server  

