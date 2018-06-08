FROM r-base:latest  
  
MAINTAINER rustr "rustr@googlegroups.com"  
  
ENV RUST_VERSION=1.14.0  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev libssl-dev \  
git curl && \  
curl -sO https://static.rust-lang.org/dist/rust-$RUST_VERSION-x86_64-unknown-
linux-gnu.tar.gz && \  
tar -xzf rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz && \  
./rust-$RUST_VERSION-x86_64-unknown-linux-gnu/install.sh \--without=rust-docs
&& \  
DEBIAN_FRONTEND=noninteractive apt-get remove \--purge -y curl && \  
DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \  
rm -rf \  
rust-$RUST_VERSION-x86_64-unknown-linux-gnu \  
rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* && \  
mkdir /source  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
apt-get update && \  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb && \  
rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
RUN R -e "install.packages(c('shiny', 'rmarkdown',
'devtools','microbenchmark','shinyAce', 'Rcpp'),
repos='https://cran.rstudio.com/');devtools::install_github('rustr/rustinr')"  
  
EXPOSE 3838  
  
COPY shiny.sh /usr/bin/shiny-server.sh  
  
RUN chmod +x /usr/bin/*.sh  
  
RUN cd /srv/shiny-server/ && git clone https://bitbucket.org/qinwf/shiny-
rustr.git  
  
CMD ["/usr/bin/shiny-server.sh"]  

