FROM ubuntu:17.04  
  
## This handle reaches Thierry  
MAINTAINER "Thierry Onkelinx" thierry.onkelinx@inbo.be  
  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Rn2k" \  
org.label-schema.description="A docker image with stable versions of R and a
bunch of packages. The full list of packages is available in the README." \  
org.label-schema.url="e.g. https://www.inbo.be/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="e.g. https://github.com/inbo/Rn2k" \  
org.label-schema.vendor="Research Institute for Nature and Forest" \  
maintainer="Thierry Onkelinx <thierry.onkelinx@inbo.be>"  
  
## Set a default user. Available via runtime flag `\--user docker`  
## Add user to 'staff' group, granting them write privileges to
/usr/local/lib/R/site.library  
## User should also have & own a home directory (for rstudio or linked volumes
to work properly).  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker \  
&& addgroup docker staff  
  
  
## script to install specific R package from CRAN  
COPY cran_install.sh cran_install.sh  
  
## copy analysis script  
COPY analysis.sh analysis.sh  
COPY analysis.R analysis.R  
  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
locales \  
&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
## Add apt-get repositories  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends dirmngr \  
&& apt-get clean \  
&& sh -c 'echo "deb http://cloud.r-project.org/bin/linux/ubuntu zesty/" >>
/etc/apt/sources.list' \  
&& gpg \--keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E084DAB9 \  
&& gpg -a --export E084DAB9 | apt-key add -  
  
## Install wget  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
&& apt-get clean  
  
## Install R base  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
r-base-core=3.4.3-1zesty0 \  
r-base-dev=3.4.3-1zesty0 \  
r-cran-boot=1.3-20-1zesty0 \  
r-cran-class=7.3-14-2zesty0 \  
r-cran-cluster=2.0.6-2zesty0 \  
r-cran-codetools=0.2-15-1 \  
r-cran-foreign=0.8.69-1zesty0 \  
r-cran-kernsmooth=2.23-15-3zesty0 \  
r-cran-lattice=0.20-35-1zesty0 \  
r-cran-mass=7.3-47-1zesty0 \  
r-cran-matrix=1.2-11-1zesty0 \  
r-cran-mgcv=1.8-22-1zesty0 \  
r-cran-nlme=3.1.131-3zesty0 \  
r-cran-nnet=7.3-12-2zesty0 \  
r-cran-rpart=4.1-11-1zesty0 \  
r-cran-spatial=7.3-11-1zesty0 \  
r-cran-survival=2.41-3-2zesty0 \  
r-recommended=3.4.3-1zesty0 \  
&& apt-get clean  
  
## Install litter  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
r-cran-littler=0.3.3-1zesty0 \  
&& apt-get clean  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libcurl4-openssl-dev \  
curl \  
git \  
libssl-dev \  
libssh2-1-dev \  
&& apt-get clean \  
&& ./cran_install.sh jsonlite 1.5 \  
&& ./cran_install.sh mime 0.5 \  
&& ./cran_install.sh curl 3.0 \  
&& ./cran_install.sh digest 0.6.14 \  
&& ./cran_install.sh R6 2.2.2 \  
&& ./cran_install.sh magrittr 1.5 \  
&& ./cran_install.sh stringi 1.1.5 \  
&& ./cran_install.sh stringr 1.2.0 \  
&& ./cran_install.sh openssl 0.9.9 \  
&& ./cran_install.sh httr 1.3.1 \  
&& ./cran_install.sh git2r 0.19.0 \  
&& ./cran_install.sh memoise 1.1.0 \  
&& ./cran_install.sh whisker 0.3-2 \  
&& ./cran_install.sh rstudioapi 0.7 \  
&& ./cran_install.sh withr 2.1.0 \  
&& ./cran_install.sh devtools 1.13.4  
  
## Install assertthat  
RUN ./cran_install.sh assertthat 0.2.0  
  
## Install dplyr and dependencies  
RUN ./cran_install.sh Rcpp 0.12.14 \  
&& ./cran_install.sh lazyeval 0.2.1 \  
&& ./cran_install.sh DBI 0.7 \  
&& ./cran_install.sh BH 1.65.0-1 \  
&& ./cran_install.sh rlang 0.1.4 \  
&& ./cran_install.sh tibble 1.3.4 \  
&& ./cran_install.sh plogr 0.1-1 \  
&& ./cran_install.sh bindr 0.1 \  
&& ./cran_install.sh pkgconfig 2.0.1 \  
&& ./cran_install.sh bindrcpp 0.2 \  
&& ./cran_install.sh glue 1.2.0 \  
&& ./cran_install.sh dplyr 0.7.4  
  
## Install plyr  
RUN ./cran_install.sh plyr 1.8.4  
  
## Install lubridate  
RUN ./cran_install.sh lubridate 1.7.1  
  
## Install freetds  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
freetds-dev \  
freetds-bin \  
tdsodbc \  
&& apt-get clean  
  
## Install RODBC and dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
pkg-config \  
libltdl7 \  
libodbc1 \  
unixodbc-dev \  
&& apt-get clean \  
&& ./cran_install.sh RODBC 1.3-15  
  
## Install xtable  
RUN ./cran_install.sh xtable 1.8-2  
  
## Install igraph and its dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libxml2-dev \  
&& ./cran_install.sh registry 0.5 \  
&& ./cran_install.sh pkgmaker 0.22 \  
&& ./cran_install.sh rngtools 1.2.4 \  
&& ./cran_install.sh gridBase 0.4-7 \  
&& ./cran_install.sh iterators 1.0.8 \  
&& ./cran_install.sh foreach 1.4.3 \  
&& ./cran_install.sh doParallel 1.0.11 \  
&& ./cran_install.sh NMF 0.20.6 \  
&& ./cran_install.sh irlba 2.3.1 \  
&& ./cran_install.sh igraph 1.1.2  
  
## install sp  
RUN ./cran_install.sh sp 1.2-5  
  
## install tidyr  
RUN ./cran_install.sh purrr 0.2.4 \  
&& ./cran_install.sh tidyselect 0.2.3 \  
&& ./cran_install.sh tidyr 0.7.2  
  
## install lme4  
RUN ./cran_install.sh minqa 1.2.4 \  
&& ./cran_install.sh nloptr 1.0.4 \  
&& ./cran_install.sh RcppEigen 0.3.3.3.1 \  
&& ./cran_install.sh lme4 1.1-14  
  
## install optimx and dependencies  
RUN ./cran_install.sh numDeriv 2016.8-1 \  
&& ./cran_install.sh optextras 2016-8.8 \  
&& ./cran_install.sh Rvmmin 2017-7.18 \  
&& ./cran_install.sh Rcgmin 2013-2.21 \  
&& ./cran_install.sh quadprog 1.5-5 \  
&& ./cran_install.sh BB 2014.10-1 \  
&& ./cran_install.sh ucminf 1.1-4 \  
&& ./cran_install.sh setRNG 2013.9-1 \  
&& ./cran_install.sh dfoptim 2016.7-1 \  
&& ./cran_install.sh svUnit 0.7-12 \  
&& ./cran_install.sh optimx 2013.8.7  
  
## install INLA  
RUN ./cran_install.sh MatrixModels 0.4-1 \  
&& wget https://github.com/inbo/INLA/archive/v17.06.20.tar.gz \  
&& R CMD INSTALL v17.06.20.tar.gz \  
&& rm v17.06.20.tar.gz  
  
## install mvtnorm  
RUN ./cran_install.sh mvtnorm 1.0-6  
  
## install multimput  
RUN wget https://github.com/inbo/multimput/archive/v0.2.8.1.tar.gz \  
&& R CMD INSTALL v0.2.8.1.tar.gz \  
&& rm v0.2.8.1.tar.gz  
  
## install aws.s3  
RUN ./cran_install.sh base64enc 0.1-3 \  
&& ./cran_install.sh aws.signature 0.3.5 \  
&& ./cran_install.sh xml2 1.1.1 \  
&& ./cran_install.sh aws.s3 0.3.3  
  
## install RPostgreSQL  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libpq-dev \  
&& ./cran_install.sh RPostgreSQL 0.6-2  
  
## install dbplyr  
RUN ./cran_install.sh dbplyr 1.1.0  
  
## install profvis  
RUN ./cran_install.sh yaml 2.1.14 \  
&& ./cran_install.sh htmltools 0.3.6 \  
&& ./cran_install.sh htmlwidgets 0.9 \  
&& ./cran_install.sh profvis 0.3.3  
  
CMD ["/bin/bash"]  

