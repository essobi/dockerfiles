FROM r-base:latest  
  
MAINTAINER Torkild U. Resheim "tur@itema.no"  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev  
  
# Download and install libssl 0.9.8  
# libssl1.0.2-dbg_1.0.2g-1_amd64.deb (squeeze14)  
RUN wget --no-verbose
http://ftp.us.debian.org/debian/pool/main/o/openssl/libssl1.0.2-dbg_1.0.2g-1_amd64.deb
&& \  
dpkg -i libssl1.0.2-dbg_1.0.2g-1_amd64.deb && \  
rm -f libssl1.0.2-dbg_1.0.2g-1_amd64.deb  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
RUN R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cran.rstudio.com/')"  
  
RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
RUN ln -sf /dev/stdout /var/log/shiny-server.log  
  
EXPOSE 3838  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
  
CMD ["/usr/bin/shiny-server.sh"]  

