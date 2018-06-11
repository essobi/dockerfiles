FROM docker.io/ubuntu:16.04  
  
MAINTAINER Michael Green micke.green@gmail.com  
  
RUN apt-get update -qq \  
&& apt-get upgrade -y  
  
RUN apt-get install -y --no-install-recommends \  
apt-transport-https \  
software-properties-common \  
curl \  
wget \  
git \  
libssl-dev \  
libcurl4-gnutls-dev \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get clean && apt-get -y update && apt-get install -y locales &&
locale-gen en_US.UTF-8  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen en_US.utf8 &&
/usr/sbin/update-locale LANG=en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
  
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu
$(lsb_release -cs)/" \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
software-properties-common ed less locales vim-tiny wget \  
ca-certificates libcurl4-openssl-dev libssl-dev \  
&& add-apt-repository --enable-source --yes "ppa:marutter/rrutter" \  
&& add-apt-repository --enable-source --yes "ppa:marutter/c2d4u"  
  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
r-base-dev \  
r-recommended \  
r-cran-devtools \  
r-cran-ggplot2 \  
r-cran-tidyr \  
r-cran-rmarkdown \  
r-cran-readr \  
r-cran-igraph \  
r-cran-diagrammer \  
pandoc \  
&& echo 'options(repos = c(CRAN = "https://cloud.r-project.org"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site \  
&& rm -rf /var/lib/apt/lists/*  
# LAtex  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
texlive \  
texlive-xetex \  
&& rm -rf /var/lib/apt/lists/*  
# Now install R and littler, and create a link for littler in /usr/local/bin  
# Also set a default CRAN repo, and make sure littler knows about it too  
# Note 1: we need wget here as the build env is too old to work with libcurl
(we think, precise was)  
# Note 2: r-cran-docopt is not currently in c2d4u so we install from source  
RUN apt-get update && apt-get install -y --no-install-recommends \  
littler r-cran-stringr r-cran-rcpp r-cran-rstan \  
&& echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site \  
&& ln -s /usr/lib/R/site-library/littler/examples/install.r
/usr/local/bin/install.r \  
&& ln -s /usr/lib/R/site-library/littler/examples/install2.r
/usr/local/bin/install2.r \  
&& ln -s /usr/lib/R/site-library/littler/examples/installGithub.r
/usr/local/bin/installGithub.r \  
&& ln -s /usr/lib/R/site-library/littler/examples/testInstalled.r
/usr/local/bin/testInstalled.r \  
&& install.r docopt \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& rm -rf /var/lib/apt/lists/*  
# Bookdown specifics  
RUN Rscript -e 'devtools::install_github("rstudio/bookdown")' \  
&& wget -c
https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-1-amd64.deb
\  
&& dpkg -i pandoc-1.19.2.1-1-amd64.deb  
  
CMD ["R"]  

