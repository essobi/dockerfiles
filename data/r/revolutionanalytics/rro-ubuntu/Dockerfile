## Example Usage:  
## docker run -v $HOME/Rdata:/data -it revolutionanalytics/rro-ubuntu R  
  
## Adapted from:  
## https://registry.hub.docker.com/u/rocker/r-base/dockerfile/  
  
## Use Ubuntu 14.04 LTS as basis for container  
FROM ubuntu:14.04  
  
MAINTAINER "Chris Mosetick" chris@revolutionanalytics.com  
  
## Start in /root, not / so checkpoint package does not attempt to scan whole
file system.  
WORKDIR /root  
  
## This is the container file system location where users can access data from
their local systems with the -v option  
VOLUME /data  
  
## Remain current  
RUN apt-get update -qq \  
&& apt-get dist-upgrade -y  
  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
ed \  
locales \  
vim-tiny \  
nano \  
wget \  
git \  
g++ \  
libcurl4-openssl-dev \  
curl  
  
## Install Revolution R Open 8.0 Beta  
RUN cd /tmp \  
&& wget
http://mran.revolutionanalytics.com/install/RRO-8.0.1-Beta3-Ubuntu-14.04.x86_64.tar.gz
\  
&& tar -xzf RRO-8.0.1-Beta3-Ubuntu-14.04.x86_64.tar.gz \  
&& ./install.sh  
  
## This is just to set a sane container wide default and is not required  
RUN mkdir /etc/R \  
&& touch /etc/R/Rprofile.site \  
&& echo 'options(repos = list(CRAN = "http://cran.revolutionanalytics.com/"))'
>> /etc/R/Rprofile.site  
  
## By default the `checkpoint` R package is in RRO.  
## Use the command below to load it into your R session  
## library("checkpoint")  
## Select a snapshot date in the past, as in the example below  
## checkpoint("2014-11-10")  
  
## Set a default user. Available via runtime flag `--user docker`  
## Add user to 'staff' group, granting them write privileges to
/usr/local/lib/R/site.library  
## User should also have & own a home directory (for rstudio or linked volumes
to work properly). (could use adduser to create this automatically instead)  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker \  
&& addgroup docker staff  
  
## Configure default locale  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  

