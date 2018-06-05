FROM ubuntu:16.04  
MAINTAINER ajay@deonarine.com  
  
RUN apt-get upgrade -y && apt-get dist-upgrade  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
build-essential \  
gdebi-core \  
libcurl4-openssl-dev \  
libssl-dev \  
libssh2-1-dev \  
r-base \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
#Add new cran repo  
RUN echo 'deb https://cloud.r-project.org/bin/linux/ubuntu xenial/' >>
/etc/apt/sources.list  
  
##And Key  
RUN gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E084DAB9  
RUN gpg -a --export E084DAB9 | apt-key add -  
  
##Upgrade R  
RUN apt-get update && apt-get upgrade -y \  
&& rm -rf /var/lib/apt/lists/*  
  
##Install R packages  
#RUN su - -c "R -e \"install.packages('shiny', repos =
'http://cran.rstudio.com/')\""  
RUN su - -c "R -e \"install.packages(c( \  
'curl', \  
'DBI', \  
'dplyr', \  
'devtools', \  
'doMC', \  
'foreach', \  
'ggplot2', \  
'ggvis', \  
'httr', \  
'jsonlite', \  
'lubridate', \  
'rbokeh', \  
'readr', \  
'Rcpp', \  
'shiny', \  
'stringr', \  
'tidyr', \  
'xml2' \  
), repos = 'http://cloud.r-project.org/')\""  
RUN wget https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-
server-1.5.1.834-amd64.deb  
  
#non-interactive mode  
RUN gdebi shiny-server-1.5.1.834-amd64.deb -n  
  
WORKDIR /home/work  
RUN cat R --version  
RUN apt-cache showpkg shiny-server  
CMD shiny-server

