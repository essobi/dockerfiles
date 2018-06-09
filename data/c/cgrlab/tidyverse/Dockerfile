FROM ubuntu:14.04  
# auto builds at cgrlab/tidyverse  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
software-properties-common \  
libcurl4-openssl-dev \  
libxml2-dev \  
libxml2-dev \  
libcairo2-dev \  
libsqlite-dev \  
libmariadbd-dev \  
libmariadbclient-dev \  
libpq-dev \  
libssh2-1-dev \  
libpng-dev \  
libglu1-mesa-dev \  
libv8-dev \  
ed \  
curl \  
wget \  
less \  
locales \  
vim-tiny \  
ca-certificates \  
&& add-apt-repository -y "ppa:marutter/rrutter" \  
&& add-apt-repository -y "ppa:marutter/c2d4u" \  
&& apt-get update  
  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
## Now install R and littler, and create a link for littler in /usr/local/bin  
## Also set a default CRAN repo, and make sure littler knows about it too  
## Note 1: we need wget here as the build env is too old to work with libcurl
(we think, precise was)  
## Note 2: r-cran-docopt is not currently in c2d4u so we install from source  
RUN apt-get install -y --no-install-recommends \  
pandoc \  
r-cran-littler \  
r-base \  
r-base-dev \  
r-recommended \  
&& R -e "source('https://bioconductor.org/biocLite.R')" \  
  
&& echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"),
download.file.method = "wget")' >> /etc/R/Rprofile.site \  
&& ln -s /usr/lib/R/site-library/littler/examples/install.r
/usr/local/bin/install.r \  
&& ln -s /usr/lib/R/site-library/littler/examples/install2.r
/usr/local/bin/install2.r \  
&& ln -s /usr/lib/R/site-library/littler/examples/installGithub.r
/usr/local/bin/installGithub.r \  
&& ln -s /usr/lib/R/site-library/littler/examples/testInstalled.r
/usr/local/bin/testInstalled.r \  
&& install.r docopt \  
  
&& install2.r --error \  
\--deps TRUE \  
tidyverse \  
dplyr \  
ggplot2 \  
devtools \  
formatR \  
remotes \  
stringi \  
knitr \  
rmarkdown \  
V8 \  
DT \  
  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  

