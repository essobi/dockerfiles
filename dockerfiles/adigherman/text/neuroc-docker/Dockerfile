## Get latest stable NeuroDebian image
FROM ubuntu:yakkety

RUN apt-get update
RUN apt-get install -y \
	dirmngr \
	wget

## Add package repo sources
RUN wget -O- http://neuro.debian.net/lists/xenial.us-tn.full | tee /etc/apt/sources.list.d/neurodebian.sources.list \
&& apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9

RUN echo "deb http://neuro.debian.net/debian wheezy main" >>  /etc/apt/sources.list.d/neurodebian.sources.list
RUN echo "deb http://neuro.debian.net/debian data main" >>  /etc/apt/sources.list.d/neurodebian.sources.list
RUN echo "deb http://us.archive.ubuntu.com/ubuntu trusty main universe" >>  /etc/apt/sources.list.d/neurodebian.sources.list
RUN echo "deb http://us.archive.ubuntu.com/ubuntu wily main universe" >>  /etc/apt/sources.list.d/neurodebian.sources.list

RUN apt-get update

## Install afni, fsl (and dependencies)
RUN apt-get install -y \
#	libgsl0ldbl \
	libgsl2 \
	libnetcdf7 \
	afni \
	fsl-complete 

## Install R
RUN apt-get install -y r-base

## Install devtools (and dependencies)
RUN apt-get install -y \
	libcurl4-gnutls-dev \
	libxml2-dev \
	libssl-dev
RUN su - -c "R -e \"install.packages('devtools', repos='http://cran.rstudio.com/')\""
