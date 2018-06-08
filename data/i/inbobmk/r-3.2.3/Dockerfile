FROM ubuntu:14.04.3  
## This handle reaches Thierry  
MAINTAINER "Thierry Onkelinx" thierry.onkelinx@inbo.be  
  
## Set a default user. Available via runtime flag `--user docker`  
## Add user to 'staff' group, granting them write privileges to
/usr/local/lib/R/site.library  
## User should also have & own a home directory (for rstudio or linked volumes
to work properly).  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker \  
&& addgroup docker staff  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
## Add apt-get repositories  
RUN sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list' \  
&& gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \  
&& gpg -a --export E084DAB9 | apt-key add -  
## Install R base  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
r-base-core=3.2.3-4trusty0 \  
r-cran-boot=1.3-17-1trusty0 \  
r-cran-cluster=2.0.3-1trusty0 \  
r-cran-foreign=0.8.66-1trusty0 \  
r-cran-mass=7.3-44-1trusty0 \  
r-cran-kernsmooth=2.23-15-1trusty0 \  
r-cran-lattice=0.20-33-1trusty0 \  
r-cran-nlme=3.1.123-1trusty0 \  
r-cran-matrix=1.2-3-1trusty0 \  
r-cran-mgcv=1.8-7-1trusty0 \  
r-cran-survival=2.38-3-1trusty0 \  
r-cran-rpart=4.1-10-1trusty0 \  
r-cran-class=7.3-14-1trusty0 \  
r-cran-nnet=7.3-11-1trusty0 \  
r-cran-spatial=7.3-10-1trusty0 \  
r-cran-codetools=0.2-14-1~ubuntu14.04.1~ppa1 \  
r-recommended=3.2.3-4trusty0 \  
r-base=3.2.3-4trusty0 \  
&& apt-get clean  
  
## Install R dev  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
r-base-dev=3.2.3-4trusty0 \  
&& apt-get clean  
  
## Install wget  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
&& apt-get clean  
  
## Install devtools and dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libcurl4-openssl-dev \  
git \  
libssl-dev \  
libssh2-1-dev \  
&& apt-get clean \  
&& wget https://github.com/cran/jsonlite/archive/0.9.19.tar.gz \  
&& R CMD INSTALL 0.9.19.tar.gz \  
&& rm 0.9.19.tar.gz \  
&& wget https://github.com/cran/mime/archive/0.4.tar.gz \  
&& R CMD INSTALL 0.4.tar.gz \  
&& rm 0.4.tar.gz \  
&& wget https://github.com/cran/curl/archive/0.9.5.tar.gz \  
&& R CMD INSTALL 0.9.5.tar.gz \  
&& rm 0.9.5.tar.gz \  
&& wget https://github.com/cran/digest/archive/0.6.9.tar.gz \  
&& R CMD INSTALL 0.6.9.tar.gz \  
&& rm 0.6.9.tar.gz \  
&& wget https://github.com/cran/R6/archive/2.1.1.tar.gz \  
&& R CMD INSTALL 2.1.1.tar.gz \  
&& rm 2.1.1.tar.gz \  
&& wget https://github.com/cran/magrittr/archive/1.5.tar.gz \  
&& R CMD INSTALL 1.5.tar.gz \  
&& rm 1.5.tar.gz \  
&& wget https://github.com/cran/stringi/archive/1.0-1.tar.gz \  
&& R CMD INSTALL 1.0-1.tar.gz \  
&& rm 1.0-1.tar.gz \  
&& wget https://github.com/cran/stringr/archive/1.0.0.tar.gz \  
&& R CMD INSTALL 1.0.0.tar.gz \  
&& rm 1.0.0.tar.gz \  
&& wget https://github.com/cran/httr/archive/1.0.0.tar.gz \  
&& R CMD INSTALL 1.0.0.tar.gz \  
&& rm 1.0.0.tar.gz \  
&& wget https://github.com/cran/git2r/archive/0.13.1.tar.gz \  
&& R CMD INSTALL 0.13.1.tar.gz \  
&& rm 0.13.1.tar.gz \  
&& wget https://github.com/cran/memoise/archive/0.2.1.tar.gz \  
&& R CMD INSTALL 0.2.1.tar.gz \  
&& rm 0.2.1.tar.gz \  
&& wget https://github.com/cran/whisker/archive/0.3-2.tar.gz \  
&& R CMD INSTALL 0.3-2.tar.gz \  
&& rm 0.3-2.tar.gz \  
&& wget https://github.com/cran/rstudioapi/archive/0.5.tar.gz \  
&& R CMD INSTALL 0.5.tar.gz \  
&& rm 0.5.tar.gz \  
&& wget https://github.com/cran/withr/archive/1.0.0.tar.gz \  
&& R CMD INSTALL 1.0.0.tar.gz \  
&& rm 1.0.0.tar.gz \  
&& wget https://github.com/cran/devtools/archive/1.10.0.tar.gz \  
&& R CMD INSTALL 1.10.0.tar.gz \  
&& rm 1.10.0.tar.gz  
## Install digest 0.6.9.1 from Github  
RUN Rscript -e 'devtools::install_github("eddelbuettel/digest", ref =
"ef7141de412aa8bd76572a0349ed69ddbaf0d979", upgrade_dependencies = FALSE)'  
  
## Install assertthat  
RUN wget https://github.com/cran/assertthat/archive/0.1.tar.gz \  
&& R CMD INSTALL 0.1.tar.gz \  
&& rm 0.1.tar.gz  
## Install dplyr and dependencies  
RUN wget https://github.com/cran/Rcpp/archive/0.12.2.tar.gz \  
&& R CMD INSTALL 0.12.2.tar.gz \  
&& rm 0.12.2.tar.gz \  
&& wget https://github.com/cran/lazyeval/archive/0.1.10.tar.gz \  
&& R CMD INSTALL 0.1.10.tar.gz \  
&& rm 0.1.10.tar.gz \  
&& Rscript -e 'devtools::install_github("rstats-db/DBI", ref =
"9da78f3074f88164fdedaa33c6848355cffe5cf9", upgrade_dependencies = FALSE)' \  
&& wget https://github.com/cran/BH/archive/1.60.0-1.tar.gz \  
&& R CMD INSTALL 1.60.0-1.tar.gz \  
&& rm 1.60.0-1.tar.gz \  
&& wget https://github.com/cran/dplyr/archive/0.4.3.tar.gz \  
&& R CMD INSTALL 0.4.3.tar.gz \  
&& rm 0.4.3.tar.gz  
## Install plyr  
RUN wget https://github.com/cran/plyr/archive/1.8.3.tar.gz \  
&& R CMD INSTALL 1.8.3.tar.gz \  
&& rm 1.8.3.tar.gz  
## Install lubridate and dependencies  
RUN wget https://github.com/cran/lubridate/archive/1.5.0.tar.gz \  
&& R CMD INSTALL 1.5.0.tar.gz \  
&& rm 1.5.0.tar.gz  
## Install RODBC  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
pkg-config \  
libltdl7 \  
libodbc1 \  
unixodbc-dev \  
&& apt-get clean \  
&& wget https://github.com/cran/RODBC/archive/1.3-12.tar.gz \  
&& R CMD INSTALL 1.3-12.tar.gz \  
&& rm 1.3-12.tar.gz  
## Install testthat and dependencies  
RUN wget https://github.com/cran/crayon/archive/1.3.1.tar.gz \  
&& R CMD INSTALL 1.3.1.tar.gz \  
&& rm 1.3.1.tar.gz \  
&& wget https://github.com/cran/praise/archive/1.0.0.tar.gz \  
&& R CMD INSTALL 1.0.0.tar.gz \  
&& rm 1.0.0.tar.gz \  
&& wget https://github.com/cran/testthat/archive/0.11.0.tar.gz \  
&& R CMD INSTALL 0.11.0.tar.gz \  
&& rm 0.11.0.tar.gz  
## Add minimal LaTeX configuration  
## Taken from https://github.com/rocker-org/hadleyverse/blob/master/Dockerfile  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
lmodern \  
qpdf \  
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
## Install pandoc  
RUN wget
https://github.com/jgm/pandoc/releases/download/1.16.0.2/pandoc-1.16.0.2-1-amd64.deb
\  
&& dpkg -i pandoc-1.16.0.2-1-amd64.deb \  
&& rm pandoc-1.16.0.2-1-amd64.deb  
## Install rmarkdown and dependencies  
RUN wget https://github.com/cran/yaml/archive/2.1.13.tar.gz \  
&& R CMD INSTALL 2.1.13.tar.gz \  
&& rm 2.1.13.tar.gz \  
&& wget https://github.com/cran/evaluate/archive/0.8.tar.gz \  
&& R CMD INSTALL 0.8.tar.gz \  
&& rm 0.8.tar.gz \  
&& wget https://github.com/cran/formatR/archive/1.2.1.tar.gz \  
&& R CMD INSTALL 1.2.1.tar.gz \  
&& rm 1.2.1.tar.gz \  
&& wget https://github.com/cran/highr/archive/0.5.1.tar.gz \  
&& R CMD INSTALL 0.5.1.tar.gz \  
&& rm 0.5.1.tar.gz \  
&& wget https://github.com/cran/markdown/archive/0.7.7.tar.gz \  
&& R CMD INSTALL 0.7.7.tar.gz \  
&& rm 0.7.7.tar.gz \  
&& wget https://github.com/cran/knitr/archive/1.12.3.tar.gz \  
&& R CMD INSTALL 1.12.3.tar.gz \  
&& rm 1.12.3.tar.gz \  
&& wget https://github.com/cran/bitops/archive/1.0-6.tar.gz \  
&& R CMD INSTALL 1.0-6.tar.gz \  
&& rm 1.0-6.tar.gz \  
&& wget https://github.com/cran/caTools/archive/1.17.1.tar.gz \  
&& R CMD INSTALL 1.17.1.tar.gz \  
&& rm 1.17.1.tar.gz \  
&& wget https://github.com/cran/htmltools/archive/0.3.tar.gz \  
&& R CMD INSTALL 0.3.tar.gz \  
&& rm 0.3.tar.gz \  
&& wget https://github.com/cran/rmarkdown/archive/0.9.2.tar.gz \  
&& R CMD INSTALL 0.9.2.tar.gz \  
&& rm 0.9.2.tar.gz  
## Install covr and dependencies  
RUN wget https://github.com/cran/rex/archive/1.0.1.tar.gz \  
&& R CMD INSTALL 1.0.1.tar.gz \  
&& rm 1.0.1.tar.gz \  
&& wget https://github.com/cran/covr/archive/1.2.0.tar.gz \  
&& R CMD INSTALL 1.2.0.tar.gz \  
&& rm 1.2.0.tar.gz  
## Install ggplot2 and dependencies  
RUN wget https://github.com/cran/colorspace/archive/1.2-6.tar.gz \  
&& R CMD INSTALL 1.2-6.tar.gz \  
&& rm 1.2-6.tar.gz \  
&& wget https://github.com/cran/munsell/archive/0.4.2.tar.gz \  
&& R CMD INSTALL 0.4.2.tar.gz \  
&& rm 0.4.2.tar.gz \  
&& wget https://github.com/cran/RColorBrewer/archive/1.1-2.tar.gz \  
&& R CMD INSTALL 1.1-2.tar.gz \  
&& rm 1.1-2.tar.gz \  
&& wget https://github.com/cran/dichromat/archive/2.0-0.tar.gz \  
&& R CMD INSTALL 2.0-0.tar.gz \  
&& rm 2.0-0.tar.gz \  
&& wget https://github.com/cran/labeling/archive/0.3.tar.gz \  
&& R CMD INSTALL 0.3.tar.gz \  
&& rm 0.3.tar.gz \  
&& wget https://github.com/cran/scales/archive/0.3.0.tar.gz \  
&& R CMD INSTALL 0.3.0.tar.gz \  
&& rm 0.3.0.tar.gz \  
&& wget https://github.com/cran/reshape2/archive/1.4.1.tar.gz \  
&& R CMD INSTALL 1.4.1.tar.gz \  
&& rm 1.4.1.tar.gz \  
&& wget https://github.com/cran/gtable/archive/0.1.2.tar.gz \  
&& R CMD INSTALL 0.1.2.tar.gz \  
&& rm 0.1.2.tar.gz \  
&& wget https://github.com/hadley/ggplot2/archive/v2.0.0.tar.gz \  
&& R CMD INSTALL v2.0.0.tar.gz \  
&& rm v2.0.0.tar.gz  
## Install igraph and its dependencies  
RUN wget https://github.com/cran/xtable/archive/1.8-0.tar.gz \  
&& R CMD INSTALL 1.8-0.tar.gz \  
&& rm 1.8-0.tar.gz \  
&& wget https://github.com/cran/registry/archive/0.3.tar.gz \  
&& R CMD INSTALL 0.3.tar.gz \  
&& rm 0.3.tar.gz \  
&& wget https://github.com/cran/pkgmaker/archive/0.22.tar.gz \  
&& R CMD INSTALL 0.22.tar.gz \  
&& rm 0.22.tar.gz \  
&& wget https://github.com/cran/rngtools/archive/1.2.4.tar.gz \  
&& R CMD INSTALL 1.2.4.tar.gz \  
&& rm 1.2.4.tar.gz \  
&& wget https://github.com/cran/gridBase/archive/0.4-7.tar.gz \  
&& R CMD INSTALL 0.4-7.tar.gz \  
&& rm 0.4-7.tar.gz \  
&& wget https://github.com/cran/iterators/archive/1.0.7.tar.gz \  
&& R CMD INSTALL 1.0.7.tar.gz \  
&& rm 1.0.7.tar.gz \  
&& wget https://github.com/cran/foreach/archive/1.4.3.tar.gz \  
&& R CMD INSTALL 1.4.3.tar.gz \  
&& rm 1.4.3.tar.gz \  
&& wget https://github.com/cran/doParallel/archive/1.0.10.tar.gz \  
&& R CMD INSTALL 1.0.10.tar.gz \  
&& rm 1.0.10.tar.gz \  
&& wget https://github.com/cran/NMF/archive/0.20.6.tar.gz \  
&& R CMD INSTALL 0.20.6.tar.gz \  
&& rm 0.20.6.tar.gz \  
&& wget https://github.com/cran/irlba/archive/2.0.0.tar.gz \  
&& R CMD INSTALL 2.0.0.tar.gz \  
&& rm 2.0.0.tar.gz \  
&& wget https://github.com/cran/igraph/archive/1.0.1.tar.gz \  
&& R CMD INSTALL 1.0.1.tar.gz \  
&& rm 1.0.1.tar.gz  
## install lintr and dependencies  
RUN wget https://github.com/cran/stringdist/archive/0.9.4.1.tar.gz \  
&& R CMD INSTALL 0.9.4.1.tar.gz \  
&& rm 0.9.4.1.tar.gz \  
&& wget https://github.com/cran/lintr/archive/0.3.3.tar.gz \  
&& R CMD INSTALL 0.3.3.tar.gz \  
&& rm 0.3.3.tar.gz  
## install sp  
RUN wget https://github.com/cran/sp/archive/1.2-2.tar.gz \  
&& R CMD INSTALL 1.2-2.tar.gz \  
&& rm 1.2-2.tar.gz  
## install tidyr  
RUN wget https://github.com/cran/tidyr/archive/0.4.1.tar.gz \  
&& R CMD INSTALL 0.4.1.tar.gz \  
&& rm 0.4.1.tar.gz  
## install lme4  
RUN wget https://github.com/cran/minqa/archive/1.2.4.tar.gz \  
&& R CMD INSTALL 1.2.4.tar.gz \  
&& rm 1.2.4.tar.gz \  
&& wget https://github.com/cran/nloptr/archive/1.0.4.tar.gz \  
&& R CMD INSTALL 1.0.4.tar.gz \  
&& rm 1.0.4.tar.gz \  
&& wget https://github.com/cran/RcppEigen/archive/0.3.2.7.0.tar.gz \  
&& R CMD INSTALL 0.3.2.7.0.tar.gz \  
&& rm 0.3.2.7.0.tar.gz \  
&& wget https://github.com/cran/lme4/archive/1.1-10.tar.gz \  
&& R CMD INSTALL 1.1-10.tar.gz \  
&& rm 1.1-10.tar.gz  
## install optimx  
RUN wget https://github.com/cran/numDeriv/archive/2014.2-1.tar.gz \  
&& R CMD INSTALL 2014.2-1.tar.gz \  
&& rm 2014.2-1.tar.gz \  
&& wget https://github.com/cran/optextras/archive/2013-10.28.tar.gz \  
&& R CMD INSTALL 2013-10.28.tar.gz \  
&& rm 2013-10.28.tar.gz \  
&& wget https://github.com/cran/optimx/archive/2014.5.4.tar.gz \  
&& R CMD INSTALL 2014.5.4.tar.gz \  
&& rm 2014.5.4.tar.gz  
## install INLA  
RUN wget https://github.com/INBO-BMK/INLA/archive/v0.0-1455098891.tar.gz \  
&& R CMD INSTALL v0.0-1455098891.tar.gz \  
&& rm v0.0-1455098891.tar.gz  
## install roxygen2 and dependencies  
RUN wget https://github.com/cran/brew/archive/1.0-6.tar.gz \  
&& R CMD INSTALL 1.0-6.tar.gz \  
&& rm 1.0-6.tar.gz \  
&& wget https://github.com/klutometis/roxygen/archive/v5.0.1.tar.gz \  
&& R CMD INSTALL v5.0.1.tar.gz \  
&& rm v5.0.1.tar.gz  
## install RSQLite  
RUN wget https://github.com/cran/RSQLite/archive/1.0.0.tar.gz \  
&& R CMD INSTALL 1.0.0.tar.gz \  
&& rm 1.0.0.tar.gz  
## Start R  
CMD ["R", "--no-save", "--no-restore"]  

