FROM rocker/tidyverse:3.3.2  
MAINTAINER Chris Haid "chaid@kippchicago.org"  
RUN apt-get update && apt-get install -y --no-install-recommends \  
sudo \  
gdebi \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev \  
libxt-dev  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
# R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cran.rstudio.com/')" && \  
# cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
# Download and install shiny server  
# RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
# VERSION=$(cat version.txt) && \  
# wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
# gdebi -n ss-latest.deb && \  
# rm -f version.txt ss-latest.deb  
# FROM rocker/shiny  
#  
#  
# # Winston Chang wrote the following to get shiny up and running.  
# RUN apt-get update -y  
# RUN apt-get install -y libssl-dev  
# RUN apt-get install -y libxml2-dev  
# RUN apt-get install -y git-core  
# RUN apt-get install -y libbz2-dev  
# RUN apt-get install -y libpcre3-dev  
# RUN apt-get install -y liblzma-dev  
#RUN apt-get install -y libssl1.0.0  
# Download and install libssl 0.9.8  
#RUN wget --no-verbose
http://ftp.us.debian.org/debian/pool/main/o/openssl/libssl0.9.8_0.9.8o-4squeeze14_amd64.deb
&& \  
# dpkg -i libssl0.9.8_0.9.8o-4squeeze14_amd64.deb && \  
# rm -f libssl0.9.8_0.9.8o-4squeeze14_amd64.deb  
## TEMPORARY to get fixed version of git2r package  
#RUN git clone https://github.com/ropensci/git2r.git \  
# && R CMD build git2r \  
# && R CMD INSTALL git2r_0.15.0.9000.tar.gz  
#RUN R -e "install.packages('devtools')"  
RUN R -e "install.packages(c('RCurl', 'rmarkdown', 'shiny', 'xtable', 'Cairo',
'shinydashboard', 'DT'), repos='https://cran.rstudio.com/')"  
  
#RUN R -e "devtools::install_github('hadley/readr')"  
RUN R -e "devtools::install_github('jennybc/googlesheets')"  
  
RUN R -e "devtools::install_github('almartin82/mapvizieR')"  
  
RUN R -e "install.packages('shiny', repos='https://cran.rstudio.com/')"  
  
RUN R -e "install.packages('htmltools', repos='https://cran.rstudio.com/')"  
  
RUN R -e "devtools::install_github('rstudio/flexdashboard')"  
  
RUN R -e "install.packages('DT')"  
  
RUN R -e "install.packages('viridis', repos='https://cran.rstudio.com/')"  
  
RUN R -e "install.packages('zoo')"  
  
RUN R -e "install.packages('timevis', repos='https://cran.rstudio.com/')"  
  
RUN R -e "install.packages('sunburstR', repos='https://cran.rstudio.com/')"  
  
RUN R -e "install.packages('networkD3', repos='https://cran.rstudio.com/')"  
  
RUN R -e "install.packages('igraph', repos='https://cran.rstudio.com/')"  
  
# Set timezone to Chicago  
RUN cp /usr/share/zoneinfo/America/Chicago /etc/localtime && \  
echo "America/Chicago" > /etc/timezone  
  
# RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
RUN rm -rf /usr/local/lib/R/site-library/shiny/examples  
  
EXPOSE 3838  
# Copy front matter to /srv/shiny-server  
RUN rm /srv/shiny-server/index.html  
COPY ./front-matter /srv/shiny-server/  
  
COPY ./recruit/ /srv/shiny-server/recruit  
  
COPY ./assets/ /var/www/  
  
COPY ./war /srv/shiny-server/war  
COPY ./map /srv/shiny-server/map  
COPY ./assignments /srv/shiny-server/assignments  
COPY ./ktc /srv/shiny-server/ktc  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
CMD ["/usr/bin/shiny-server.sh"]  

