FROM opencpu/base  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-utils \  
libnlopt-dev \  
clang \  
ccache \  
littler \  
r-cran-littler  
  
RUN echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site  
RUN echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r  
  
RUN if [ ! -e /usr/local/bin/install.r ]; then ln -s
/usr/share/doc/littler/examples/install.r /usr/local/bin/install.r; fi  
RUN if [ ! -e /usr/local/bin/install2.r ]; then ln -s
/usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r; fi  
  
RUN install.r docopt  
  
RUN rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
RUN rm -rf /var/lib/apt/lists/*  
  
# ---  
RUN mkdir -p /root/.R/ && echo "\nCC=clang\n" >> /root/.R/Makevars && echo
"\nCXX=clang++\n" >> /root/.R/Makevars  
RUN install2.r --error rstanarm  
RUN rm -rf /root/.R  
  
RUN install2.r --error data.table  
RUN install2.r --error futile.logger  
RUN install2.r --error glue  
RUN install2.r --error googleCloudStorageR  
RUN install2.r --error lattice  
RUN install2.r --error MASS  
RUN install2.r --error mockery  
RUN install2.r --error purrr  
RUN install2.r --error tidyr  
RUN install2.r --error roxygen2  
RUN install2.r --error bigQueryR  
  
# put new packages here  

