# ---------------------------------------------
#
# Dockerfile best practices
# Refer: http://docs.docker.com/engine/articles/dockerfile_best-practices/
#
# This file makes use of contributions from Rafal Szkup, Application Engineer, UoA
# and the iNZight Team, UoA
#
# ---------------------------------------------

# start with a light-weight base image
FROM debian:jessie

MAINTAINER "Science IS Team" ws@sit.auckland.ac.nz

ENV BUILD_DATE "2016-12-15"

# Add the CRAN PPA to get all versions of R and install base R and required packages
# install shiny server and clean up all downloaded files to make sure the image remains lean as much as possible
# NOTE: we group a lot of commands together to reduce the number of layers that Docker creates in building this image

COPY shiny-server.sh /opt/

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 381BA480 \
    && echo "deb http://cran.stat.auckland.ac.nz/bin/linux/debian jessie-cran3/" | tee -a /etc/apt/sources.list.d/R.list \
    && apt-get update \
    && apt-get install -y -q \
        r-base-core \
        libssl-dev \
        libssl1.0.0 \
        sudo \
        wget \
    && wget --no-verbose -O libssl.deb http://ftp.us.debian.org/debian/pool/main/o/openssl/libssl0.9.8_0.9.8o-4squeeze14_amd64.deb \
    && dpkg -i libssl.deb \
    && rm -f libssl.deb \
    && R -e "install.packages(c('rmarkdown', 'shiny', 'DT'), repos='http://cran.rstudio.com/', lib='/usr/lib/R/site-library')" \
    && wget --no-verbose -O shiny-server.deb https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-server-1.5.1.834-amd64.deb \
    && dpkg -i shiny-server.deb \
    && chmod +x /opt/shiny-server.sh \
    && rm -f shiny-server.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# expose ports
EXPOSE 3838

# we do NOT initiate any process - treat this image as abstract class equivalent

