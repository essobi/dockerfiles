### A Docker file to build and prepare a testing environment for ETX R
packages  
  
FROM debian:jessie  
  
MAINTAINER "Adam Sardar" adam.sardar@etherapeutics.co.uk  
  
## Much of this docker file was shamelessly copied from the rocker/r-base file  
  
## Set a default user. Available via runtime flag `--user docker`  
## Add user to 'staff' group, granting them write privileges to
/usr/local/lib/R/site.library  
## User should also have & own a home directory (for rstudio or linked volumes
to work properly).  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker \  
&& addgroup docker staff  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ed \  
less \  
locales \  
vim-tiny \  
wget \  
unzip \  
sudo \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
  
#Add the most jessie CRAN mirror to our sources list  
RUN echo "deb http://www.stats.bris.ac.uk/R/bin/linux/debian jessie-cran3/" >
/etc/apt/sources.list.d/jessie-cran3.list  
  
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480  
  
ENV R_BASE_VERSION 3.2.2  
  
## Now install R and littler, and create a link for littler in /usr/local/bin  
## Also set a default CRAN repo, and make sure littler knows about it too  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
littler \  
r-base=${R_BASE_VERSION}* \  
r-base-dev=${R_BASE_VERSION}* \  
r-recommended=${R_BASE_VERSION}* \  
&& echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site \  
&& echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \  
&& ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r \  
&& ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r
\  
&& ln -s /usr/share/doc/littler/examples/installGithub.r
/usr/local/bin/installGithub.r \  
&& ln -s /usr/share/doc/littler/examples/testInstalled.r
/usr/local/bin/testInstalled.r \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
file \  
git \  
libapparmor1 \  
libedit2 \  
libcurl4-openssl-dev \  
libssl-dev \  
psmisc \  
supervisor \  
pandoc \  
&& rm -rf /var/lib/apt/lists/*  
  
  
## LaTeX:  
## This installs inconsolata fonts used in R vignettes/manuals manually since
texlive-fonts-extra is HUGE  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
aspell \  
aspell-en \  
ghostscript \  
imagemagick \  
lmodern \  
texlive-fonts-recommended \  
texlive-humanities \  
texlive-latex-extra \  
texinfo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& cd /usr/share/texlive/texmf-dist \  
&& wget http://mirrors.ctan.org/install/fonts/inconsolata.tds.zip \  
&& unzip inconsolata.tds.zip \  
&& rm inconsolata.tds.zip \  
&& echo "Map zi4.map" >> /usr/share/texlive/texmf-dist/web2c/updmap.cfg \  
&& mktexlsr \  
&& updmap-sys  
  
## Install some external dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libcairo2-dev \  
libssl-dev \  
r-cran-cairodevice \  
libcairo2-dev \  
libxcb1-dev \  
libxdmcp-dev \  
libxml2-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
RUN install.r stringr docopt  
  
RUN install2.r --error \  
Matrix \  
MASS \  
igraph \  
igraphdata \  
data.table \  
magrittr \  
ensurer \  
doParallel \  
foreach \  
iterators \  
foreach \  
devtools \  
dplyr \  
ggplot2 \  
shiny \  
knitr \  
R.utils \  
reshape2 \  
rmarkdown \  
testthat \  
assertthat \  
ensurer \  
xtable \  
latex2exp \  
jsonlite \  
Rcpp \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(pkgs=
c( \  
"BiocInstaller", \  
"BioNet", \  
"SANTA", \  
"limma"))'  
  
#Install httr  
RUN install2.r --error \  
httr  
  
## httr authentication uses this port  
EXPOSE 1410  
ENV HTTR_LOCALHOST 0.0.0.0  

