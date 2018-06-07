FROM dit4c/dit4c-container-ipython:latest  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
# Install R  
# - R  
# - libcurl-devel (necessary for RCurl package, a dependency of devtools)  
RUN echo "deb https://cran.csiro.au/bin/linux/debian jessie-cran3/" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480 && \  
apt-get update && \  
apt-get install -y r-base libcurl4-openssl-dev libssl-dev && \  
apt-get clean  
RUN Rscript -e \  
" options(repos=structure(c(CRAN='https://cran.csiro.au'))); \  
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ',
'devtools', 'uuid', 'digest', 'RCurl', 'openssl', 'httr', 'git2r')); \  
devtools::install_github('IRkernel/IRkernel'); \  
IRkernel::installspec(user = FALSE)"  

