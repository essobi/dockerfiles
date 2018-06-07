FROM r-base:latest  
  
MAINTAINER Kenton White "kenton.white@advancedsymbolics.com"  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5  
  
RUN apt-get update && apt-get install -f -t unstable -y --no-install-
recommends \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev \  
libxml2-dev \  
tzdata=2016c-0+deb8u1 \  
openjdk-7-* \  
r-cran-rjava \  
libgdal-dev \  
libproj-dev \  
texlive-full  
  
# Download and install libssl 0.9.8  
# RUN wget --no-verbose
http://ftp.us.debian.org/debian/pool/main/o/openssl/libssl0.9.8_0.9.8o-4squeeze14_amd64.deb
&& \  
# dpkg -i libssl0.9.8_0.9.8o-4squeeze14_amd64.deb && \  
# rm -f libssl0.9.8_0.9.8o-4squeeze14_amd64.deb  
RUN R CMD javareconf  
  
# Download and install shiny server  
RUN wget --no-verbose --no-check-certificate https://s3.amazonaws.com/rstudio-
shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose --no-check-certificate "https://s3.amazonaws.com/rstudio-
shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O
ss-latest.deb && \  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
RUN R -e "install.packages('devtools', dependencies = TRUE,
repos='http://cran.rstudio.com/')"  
RUN R -e "devtools::install_github('johnmyleswhite/ProjectTemplate')"  
RUN R -e "install.packages(c('ggvis', 'reshape', 'plyr', 'dplyr', 'stringr',
'lubridate', 'changepoint', 'devtools'), dependencies = TRUE,
repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('shiny', dependencies = TRUE,
repos='http://cran.rstudio.com/')"  
# RUN apt-get install -t unstable -y --no-install-recommends libxml2-dev  
# RUN apt-get install -t unstable -y --no-install-recommends r-cran-rjava
libgdal1-dev libproj-dev  
RUN R -e "install.packages(c('XML', 'RJDBC'), dependencies=TRUE,
repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages(c('rgdal'), dependencies=TRUE,
repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('RJSONIO', dependencies = TRUE,
repos='http://cran.rstudio.com/')"  
RUN R -e "devtools::install_github('kentonwhite/esReader')"  
RUN R -e "devtools::install_github('rstudio/leaflet')"  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
# COPY myapp /srv/shiny-server/  
EXPOSE 80  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
CMD ["/usr/bin/shiny-server.sh"]  

