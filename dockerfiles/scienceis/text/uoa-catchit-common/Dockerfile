# ---------------------------------------------
#
# Dockerfile best practices
# Refer: http://docs.docker.com/engine/articles/dockerfile_best-practices/
#
# This file makes use of contributions from Rafal Szkup, Application Engineer, UoA
# and the Catch IT Team, UoA
#
# ---------------------------------------------

# start with a light-weight base image
FROM debian:jessie

MAINTAINER "Science IS Team" ws@sit.auckland.ac.nz

# Add the CRAN PPA to get all versions of R and install base R and required packages
# install shiny server and clean up all downloaded files to make sure the image remains lean as much as possible
# NOTE: we group a lot of commands together to reduce the number of layers that Docker creates in building this image

COPY key.txt /tmp/

RUN apt-key add /tmp/key.txt \
    && echo "deb http://cran.stat.auckland.ac.nz/bin/linux/debian jessie-cran3/" | tee -a /etc/apt/sources.list.d/R.list \
    && apt-get update \
    && apt-get install -y -q \
        r-base-core \
        libcurl4-openssl-dev \
        libxml2-dev \
        libssl-dev \
        libssl1.0.0 \
        sudo \
        wget \
    && wget --no-verbose -O libssl.deb http://security.ubuntu.com/ubuntu/pool/universe/o/openssl098/libssl0.9.8_0.9.8o-7ubuntu3.2_amd64.deb \
    && dpkg -i libssl.deb \
    && rm -f libssl.deb \
    && R -e "install.packages(c('rmarkdown', 'devtools', 'shiny', 'RColorBrewer', 'prettyR', 'gplots'), repos='http://cran.rstudio.com/', lib='/usr/lib/R/site-library', dependencies=T)" \
    && R -e "devtools::install_github('AnalytixWare/ShinySky')" \
    && wget --no-verbose -O shiny-server.deb https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-server-1.4.0.756-amd64.deb \
    && dpkg -i shiny-server.deb \
    && rm -f shiny-server.deb \
    && apt-get clean \
    && rm -rf /srv/shiny-server/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

# expose ports
EXPOSE 3838

# since this forms the base image, we do NOT intend to start any process
# treat this like abstract class :)

