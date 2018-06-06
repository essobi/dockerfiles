FROM rocker/r-devel  
MAINTAINER <sascha.herrmann.consulting@gmail.com>  
  
# Install some additional tools (nano ssh git svn) to make the container more
useable  
# (libxml2-dev and libssl-dev) are necessary for R build tools  
# Finally clean up apt  
RUN apt-get update && \  
apt-get -y install nano ssh libssh2-1-dev git subversion && \  
apt-get -y install libxml2-dev libssl-dev && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Install r build tools  
RUN echo 'install.packages(c("devtools","roxygen2","testthat"),
repos="http://cran.rstudio.com/")' | R --vanilla  
  

