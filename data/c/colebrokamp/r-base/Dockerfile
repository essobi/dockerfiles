FROM ubuntu:14.04  
  
MAINTAINER "Cole Brokamp" cole.brokamp@gmail.com  
  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list \  
&& apt-get update && apt-get install -y --force-yes \  
libproj-dev \  
libgdal-dev \  
libxml2-dev \  
libssh2-1-dev \  
libcurl4-openssl-dev \  
r-base-core \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# set default CRAN repo and DL method  
RUN echo 'options(repos=c(CRAN = "https://cran.rstudio.com/"),
download.file.method="libcurl")' >> /etc/R/Rprofile.site  
  
# install devel version of automagic package to install package dependencies  
RUN R -e "install.packages('remotes'); remotes::install_github('cole-
brokamp/automagic')"  

