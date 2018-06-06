FROM r-base:3.4.4  
  
MAINTAINER Simon Coetzee "simon.coetzee@cshs.org"  
# Install dependencies and Download and install shiny server  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libxml2-dev \  
libssl-dev \  
libcairo2-dev/unstable \  
git \  
libxt-dev && \  
wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb && \  
R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cran.rstudio.com/')"  
  
RUN R -e "source('https://bioconductor.org/biocLite.R'); biocLite(c('tidyr',
'ggplot2', 'DESeq2', 'edgeR', 'iheatmapr', 'tidyverse', 'readr', 'dplyr',
'shinyjs', 'plotly', 'shinythemes', 'shinyBS', 'apeglm', 'ashr', 'DT'))" && \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/alpreyes/GENAVi.git /srv/shiny-server/GENAVi
&& \  
ln -s /srv/shiny-server/GENAVi/GENAVi.R /srv/shiny-server/GENAVi/app.R  
  
EXPOSE 3838  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
CMD ["/usr/bin/shiny-server.sh"]  

