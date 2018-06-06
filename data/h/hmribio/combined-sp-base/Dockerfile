FROM openanalytics/r-base  
  
MAINTAINER Carlos Riveros "carlos.riveros@hmri.org.au"  
ARG http_proxy  
ARG https_proxy  
  
RUN apt-get update && apt-get install -y \  
sudo \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev \  
libxt-dev \  
libssl-dev \  
libssh2-1-dev \  
libssl1.0.0  
  
# system library dependency for the euler app  
RUN apt-get update && apt-get install -y \  
libmpfr-dev  
  
# packages needed for basic shiny functionality  
RUN R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cloud.r-project.org')"  
  
# install dependencies of the euler app  
RUN R -e "install.packages('Rmpfr', repos='https://cloud.r-project.org/')"  
  
# Get the demo package from the shinyproxy-demo repo  
RUN wget https://github.com/openanalytics/shinyproxy-
demo/raw/master/shinyproxy_0.0.1.tar.gz -O /root/shinyproxy_0.0.1.tar.gz  
  
# install shinyproxy package with demo shiny application  
RUN R CMD INSTALL /root/shinyproxy_0.0.1.tar.gz  
RUN rm /root/shinyproxy_0.0.1.tar.gz  
  
# copy the app to the image  
RUN mkdir /root/euler  
COPY euler /root/euler  
  
# set host and port  
COPY Rprofile.site /usr/lib/R/etc/  
  
# EXPOSE 3838  
CMD ["R", "-e", "shiny::runApp('/root/euler')"]  

