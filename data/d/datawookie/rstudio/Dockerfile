#
=============================================================================  
# RSTUDIO DOCKER IMAGE  
#
=============================================================================  
#  
# To build:  
#  
# $ docker build -t rstudio:latest .  
#  
# To force a rebuild:  
#  
# $ docker build --no-cache -t rstudio:latest .  
#  
# To run:  
#  
# $ docker run -d -p 80:8787 --name rstudio rstudio:latest  
#  
#
\-----------------------------------------------------------------------------  
#  
FROM rocker/verse:3.4.1  
MAINTAINER Andrew Collier <andrew@exegetic.biz>  
#  
# Install system software.  
#  
# xvfb - for R packages which require X11 to install  
#  
RUN apt-get update && \  
apt-get install -y -qq \  
whois \  
apg \  
ggobi \  
libatlas3-base \  
libcurl4-openssl-dev \  
libglu1-mesa-dev \  
libgtk2.0-dev \  
libnlopt-dev \  
libtcl8.6 libtk8.6 \  
lsb-release \  
mesa-common-dev \  
unixodbc-dev \  
xvfb && \  
apt-get clean -y  
  
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
#  
# This currently doesn't work because there isn't a separate repository for
"stretch".  
#  
# RUN echo "deb https://cloud.r-project.org/bin/linux/ubuntu/ $(lsb_release
-sc)/" >>/etc/apt/sources.list  
# RUN echo "deb http://cloud.r-project.org/bin/linux/debian jessie-cran34/"
>>/etc/apt/sources.list  
  
# Consolidate locations used to install R packages from Ubuntu repository.  
#  
# RUN ln -s /usr/local/lib/R/ /usr/lib/R  
  
# Select a CRAN mirror.  
#  
# RUN echo 'options(repos = c(CRAN = "https://cran.rstudio.com"))'
>>/etc/R/Rprofile.site  
  
# Install R packages.  
#  
# The base image has packages from http://tidyverse.org/.  
#  
RUN install2.r --error --deps TRUE -- --no-test-load \  
RUnit \  
XML  
#  
# \- Packages not available on CRAN.  
#  
RUN install2.r --error --deps TRUE \  
\--repos 'http://www.bioconductor.org/packages/release/bioc' \  
graph \  
RBGL \  
pkgDepTools \  
Rgraphviz  
#  
# \- Packages on CRAN (and that rely on X11).  
#  
# RUN xvfb-run install2.r --error -- --no-test-load \  
# rattle  
#  
# \- Packages on CRAN.  
#  
RUN install2.r --error -- --no-test-load \  
adabag \  
binman \  
caret \  
corrgram \  
DiagrammeR \  
DMwR \  
e1071 \  
ElemStatLearn \  
Epi \  
fastAdaboost \  
glmnet \  
ipred \  
ISLR \  
Metrics \  
mice \  
mlbench \  
neuralnet \  
outliers \  
party \  
partykit \  
randomForest \  
rattle \  
rpart.plot \  
Rlof \  
ROCR \  
rpart \  
RSelenium \  
semver \  
vcdExtra \  
VIM \  
wdman \  
xgboost  
  
#  
# \- Packages on GitHub.  
#  
RUN R -e 'devtools::install_github("DataWookie/exegetic")'  
#  
# Add script to generate new user accounts.  
#  
ADD https://raw.githubusercontent.com/DataWookie/docker-exegetic/master/users-
create-accounts.sh /usr/sbin  
RUN chmod 700 /usr/sbin/users-create-accounts.sh  
  
# Clean up.  
#  
RUN apt-get remove -y -qq \  
xvfb  

