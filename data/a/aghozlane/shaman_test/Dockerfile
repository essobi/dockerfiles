FROM ubuntu:16.04  
  
MAINTAINER Amine Ghozlane "amine.ghozlane@pasteur.fr"  
#pandoc-citeproc pandoc sudo  
  
RUN apt-get update && apt-get install -y \  
r-base \  
wget \  
gdebi-core \  
libcurl4-openssl-dev\  
libcairo2-dev \  
libjpeg-dev \  
libtiff5-dev \  
libxt-dev \  
libxml2-dev \  
libxml2 \  
git \  
libssl-dev \  
libssh2-1-dev \  
libnlopt-dev \  
python3-pip \  
python3-yaml \  
gcc \  
gfortran \  
g++ \  
make \  
openjdk-8-jdk  
  
RUN pip3 install bioblend python-daemon  
  
#Download and install shiny server  
RUN wget --no-verbose https://cran.r-project.org/src/base/R-3/R-3.1.2.tar.gz
-P /opt/ && \  
tar -zxf /opt/R-3.1.2.tar.gz -C /opt && rm /opt/R-3.1.2.tar.gz && \  
cd /opt/R-3.1.2/ && ./configure --with-x=no && \  
make -j 4 && make install && cd / && rm -rf /opt/R-3.1.2 && \  
wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
RUN R -e """install.packages('devtools',repos='http://cran.univ-
paris1.fr/');devtools::install_github(c('aghozlane/nlme'));
install.packages(c('digest', 'gtable', 'plyr', 'reshape2',
'scales','lazyeval', 'lme4', 'assertthat', 'R6', 'DBI', 'BH','glue', 'purrr',
'rlang','knitr', 'checkmate', 'htmlwidgets'), repos='http://cran.univ-
paris1.fr/');install.packages(c('http://cran.r-project.org/src/contrib/Archive/ggplot2/ggplot2_2.1.0.tar.gz','http://cran.r-project.org/src/contrib/Archive/tibble/tibble_1.3.0.tar.gz',
'http://cran.r-project.org/src/contrib/Archive/tidyselect/tidyselect_0.2.2.tar.gz',
'http://cran.r-project.org/src/contrib/Archive/htmlTable/htmlTable_1.9.tar.gz'),
repos=NULL, type='source');library(tibble);
install.packages('http://cran.r-project.org/src/contrib/Archive/dplyr/dplyr_0.5.0.tar.gz',
repos=NULL, type='source');install.packages(c('shiny', 'shinydashboard',
'shinythemes', 'shinyjs', 'Rcpp', 'rjson', 'psych',
'vegan','dendextend','circlize', 'googleVis', 'DT', 'RColorBrewer', 'ade4',
'scales', 'gplots', 'maps','animation', 'clusterGeneration', 'coda',
'combinat', 'msm', 'numDeriv', 'plotrix', 'scatterplot3d', 'quadprog',
'igraph', 'fastmatch', 'sendmailR','shinyBS','flexdashboard', 'backports',
'readr', 'jsonlite', 'shinyFiles', 'philentropy', 'png', 'ellipse'),
repos='http://cran.univ-paris1.fr/');
source('http://bioconductor.org/biocLite.R'); biocLite(c('BiocInstaller',
'genefilter', 'DESeq2')); options(download.file.method = 'wget');
library(backports); devtools::install_github(c('aghozlane/biomformat',
'aghozlane/rNVD3', 'timelyportfolio/d3vennR', 'aghozlane/d3heatmap',
'aghozlane/scatterD3', 'pierreLec/treeWeightD3', 'aghozlane/shinydashboard',
'aghozlane/ape', 'aghozlane/phangorn', 'aghozlane/phytools',
'aghozlane/GUniFrac', 'pierreLec/PhyloTreeMetaR', 'pierreLec/KronaR',
'mangothecat/shinytoastr', 'aghozlane/shinyWidgets'))"""  
  
  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
  
RUN git clone https://github.com/aghozlane/shaman.git /srv/shiny-server/shaman
&& \  
git clone https://github.com/pierreLec/KronaRShy.git /srv/shiny-
server/kronarshy && \  
git clone https://github.com/aghozlane/shaman_bioblend.git
/usr/bin/shaman_bioblend && \  
mv /srv/shiny-server/shaman/* /srv/shiny-server/ && \  
rm -rf /srv/shiny-server/shaman && \  
chown -R shiny.shiny /srv/shiny-server/  
  
  
EXPOSE 80  
  
EXPOSE 5438  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
COPY run_kronarshy.R /usr/bin/run_kronarshy.R  
  
CMD ["/usr/bin/shiny-server.sh"]  

