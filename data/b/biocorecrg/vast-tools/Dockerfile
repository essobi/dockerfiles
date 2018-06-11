FROM rocker/r-ver:3.3.1  
# File Author / Maintainer  
MAINTAINER Toni Hermoso Pulido <toni.hermoso@crg.eu>  
  
ARG BOWTIE_VERSION=1.2.1.1  
ARG VASTTOOLS_VERSION=2.0.2  
# Install external dependencies  
RUN apt-get update -qq && apt-get install -y --no-install-recommends python
curl libcurl4-openssl-dev libssl-dev libsqlite3-dev libxml2-dev qpdf git  
  
# Install bowtie  
RUN cd /usr/local; curl --fail --silent --show-error --location --remote-name
https://github.com/BenLangmead/bowtie/releases/download/v$BOWTIE_VERSION/bowtie-${BOWTIE_VERSION}-linux-x86_64.zip  
RUN cd /usr/local; unzip -d /usr/local
bowtie-${BOWTIE_VERSION}-linux-x86_64.zip  
  
RUN cd /usr/local; rm bowtie-${BOWTIE_VERSION}-linux-x86_64.zip  
  
# Let's put in PATH  
RUN cd /usr/local/bin; ln -s ../bowtie-${BOWTIE_VERSION}/bowtie* .  
  
COPY deps.R /usr/local  
  
RUN Rscript /usr/local/deps.R  
  
# Install Vast-tools  
RUN cd /usr/local; curl --fail --silent --show-error --location --remote-name
https://github.com/vastgroup/vast-tools/archive/v${VASTTOOLS_VERSION}.tar.gz  
RUN cd /usr/local; tar zxf v${VASTTOOLS_VERSION}.tar.gz  
RUN cd /usr/local; rm v${VASTTOOLS_VERSION}.tar.gz  
  
VOLUME /VASTDB  
  
RUN cd /usr/local/vast-tools-${VASTTOOLS_VERSION}; ln -s /VASTDB .  
  
RUN cd /usr/local/vast-tools-${VASTTOOLS_VERSION}; ./install.R  
  
# Let's put in PATH  
RUN cd /usr/local/bin; ln -s ../vast-tools-${VASTTOOLS_VERSION}/vast-tools .  
  
# Clean cache  
RUN apt-get clean  
RUN set -x; rm -rf /var/lib/apt/lists/*  
  
# Shared mounting  
VOLUME /share  
  

