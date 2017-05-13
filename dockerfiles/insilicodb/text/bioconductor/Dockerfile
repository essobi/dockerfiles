FROM ubuntu:15.10
RUN echo 'deb http://cran.rstudio.com/bin/linux/ubuntu wily/' >> /etc/apt/sourdes.list

RUN apt-get update && apt-get install -y \
	libssh2-1-dev \
	libcurl4-openssl-dev \
	icu-devtools \
	libssl-dev \
	libxml2-dev \
	r-bioc-biobase
