FROM r-base:latest  
  
LABEL maintainer="inge.amlienæpsykologi.uio.no"  
  
#RUN apt-get update && apt-get install -y -t unstable \  
# gnupg  
# Install dependencies and Download and install shiny server  
#RUN echo "deb http://archive.ubuntu.com/ubuntu `cat
/etc/container_environment/DISTRIB_CODENAME`-backports main restricted
universe" >> /etc/apt/sources.list  
#RUN (echo "deb http://cran.mtu.edu/bin/linux/ubuntu `cat
/etc/container_environment/DISTRIB_CODENAME`/" >> /etc/apt/sources.list &&
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9)  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcairo2-dev/unstable \  
libapparmor1 \  
libcurl4-openssl-dev \  
libxml2-dev \  
libssl-dev \  
libxt-dev && \  
wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
#RUN R -e "install.packages(c('shiny', 'rmarkdown', 'tidyverse', 'rio',
'svglite', 'plotly', 'stargazer', 'packrat'),
repos='https://cran.rstudio.com/')"  
COPY INSTALL.R /INSTALL.R  
RUN Rscript /INSTALL.R  
  
RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ &&
\  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3838  
COPY docker/shiny-server.sh /usr/bin/shiny-server.sh  
RUN chown shiny.shiny /usr/bin/shiny-server.sh && chmod +x /usr/bin/shiny-
server.sh  
  
CMD ["/usr/bin/shiny-server.sh"]  

