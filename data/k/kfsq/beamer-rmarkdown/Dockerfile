FROM ubuntu:16.04  
  
LABEL org.label-schema.vcs-url="https://github.com/kfsq/gitlab-ci-docker" \  
org.label-schema.vendor="Docker images for use with GitLab CI" \  
maintainer="Kristoffer Winther Balling <kfsq@novonordisk.com>"  
  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | \  
tee -a /etc/apt/sources.list \  
&& gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \  
&& gpg -a --export E084DAB9 | apt-key add - \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
# Install R and build essentials (Rcpp etc)  
r-base \  
build-essential \  
## Ubuntu packages for TeX and rmarkdown  
texlive-xetex \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
lmodern \  
pandoc \  
## Ubuntu packages for including .ps files  
ghostscript \  
## Ubuntu packages for add-apt-repo and Fira install script  
software-properties-common \  
wget \  
sudo \  
## Xaringan and decktape  
curl \  
libpython2.7 \  
libx11-xcb1 \  
libxcomposite-dev \  
libxcursor-dev \  
libxdamage-dev \  
libxtst-dev \  
libnss3 \  
chromium-browser \  
libgconf-2-4 \  
&& curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& apt-get install -y nodejs \  
&& npm install decktape \  
## Install Metropolis theme for Beamer presentations  
&& add-apt-repository -y ppa:edd/misc \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
latex-metropolis \  
## Install Fira font  
&& wget https://raw.githubusercontent.com/stevebscott/steves-bash-
utils/master/install-fira.sh \  
&& sh install-fira.sh \  
## Install R packages  
&& Rscript -e "install.packages(c( \  
'knitr', \  
'rmarkdown', \  
'xaringan', \  
'ggplot2', \  
'reticulate' \  
), repos = 'http://cran.rstudio.com')" \  
## Clean up  
&& cd / \  
&& rm -rf /tmp/* \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /Fira-master \  
&& rm -rf /master.zip \  
&& rm -rf /install-fira.sh  

