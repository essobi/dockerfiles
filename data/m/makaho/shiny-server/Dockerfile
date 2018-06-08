############################################################  
# Dockerfile to build container with shiny server to run  
# genomics analysis suite  
# Based on r-base  
############################################################  
FROM r-base:latest  
  
# File Author / Maintainer  
MAINTAINER Matthias Becker <mbecker@uni-bonn.de>  
  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev \  
libssl-dev \  
libv8-dev \  
libxml2-dev \  
libcairo2-dev \  
libsqlite-dev \  
libmariadbd-dev \  
libpq-dev \  
libssh2-1-dev \  
openjdk-8-jre \  
r-cran-rjava  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
# Java is at: /usr/lib/jvm/java-8-openjdk-amd64/jre/  
RUN export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre  
RUN export PATH=$PATH:$JAVA_HOME/bin  
  
RUN R -e "install.packages(c('ReporteRs'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('ReporteRsjars'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('shiny'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('rmarkdown'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('shinyjs'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('shinyBS'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('RColorBrewer'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
  
RUN R -e "install.packages(c('stringr'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('formula.tools'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('yarrr'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('data.table'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('fdrtool'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('VennDiagram'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('colorspace'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('gplots'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('webshot'), dependencies = TRUE,
repos='https://cran.rstudio.com/') ; library(webshot) ;
webshot::install_phantomjs()"  
  
RUN R -e "install.packages(c('WGCNA'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('ape'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('V8'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('htmlwidgets'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('ggrepel'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('svglite'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
  
RUN R -e "install.packages('devtools')"  
RUN R -e "devtools::install_github('rstudio/DT')"  
RUN R -e "devtools::install_github('ropensci/plotly') ; library(plotly)"  
RUN R -e "devtools::install_github('rstudio/crosstalk',force=TRUE) ;
library(crosstalk)"  
  
RUN R -e "library('rmarkdown')"  
RUN R -e "library('shiny')"  
RUN R -e "library('shinyjs')"  
RUN R -e "library('shinyBS')"  
RUN R -e "library('RColorBrewer')"  
RUN R -e "library('stringr')"  
RUN R -e "library('formula.tools')"  
RUN R -e "library('yarrr')"  
RUN R -e "library('data.table')"  
RUN R -e "library('fdrtool')"  
RUN R -e "library('VennDiagram')"  
RUN R -e "library('colorspace')"  
RUN R -e "library('gplots')"  
RUN R -e "library('webshot')"  
  
#########packages to install  
RUN R -e "source('https://bioconductor.org/biocLite.R') ; biocLite() ;
biocLite('tximport') ; library(tximport) ; biocLite('DESeq2') ;
library(DESeq2) ; biocLite('clusterProfiler') ;library(clusterProfiler) ;
biocLite('org.Hs.eg.db') ; library(org.Hs.eg.db) ; biocLite('org.Dm.eg.db') ;
biocLite('org.Mmu.eg.db') ; library(org.Dm.eg.db) ; library(org.Mmu.eg.db) ;
biocLite('sva') ; library('sva') ; biocLite('limma') ; library('limma') ;
biocLite('annotate'); library('annotate'); biocLite('geneplotter') ;
library(geneplotter) ; biocLite('biomaRt') ; library(biomaRt) ;
biocLite('pcaGoPromoter') ; library(pcaGoPromoter) ;
biocLite('pcaGoPromoter.Mm.mm9') ; library(pcaGoPromoter.Mm.mm9) ;
biocLite('pcaGoPromoter.Hs.hg19') ; library(pcaGoPromoter.Hs.hg19) ;
biocLite(c('AnnotationDbi', 'impute', 'GO.db', 'preprocessCore'));
biocLite('pathview'); library('pathview') "  
  
RUN R -e "source('https://bioconductor.org/biocLite.R') ; biocLite() ;
biocLite('org.Mm.eg.db') ; "  
RUN R -e "install.packages(c('WGCNA'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('pheatmap'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
RUN R -e "source('https://bioconductor.org/biocLite.R') ; biocLite() ;
biocLite('topGO') ; "  
RUN R -e "source('https://bioconductor.org/biocLite.R') ; biocLite() ;
biocLite('Rgraphviz') ; "  
RUN R -e "source('https://bioconductor.org/biocLite.R') ; biocLite() ;
biocLite('GSEABase') ; "  
  
RUN apt-get install -y libudunits2-dev  
RUN apt-get install -y libgdal-dev libproj-dev  
RUN R -e "install.packages('udunits2', type = 'source', repo =
'cran.rstudio.com')"  
RUN R -e "install.packages('units', type = 'source')"  
RUN R -e "install.packages(c('plotly'), dependencies = TRUE,
repos='https://cran.rstudio.com/')"  
  
RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
EXPOSE 3838  
RUN echo "\nR_MAX_NUM_DLLS=200" >> /etc/R/Renviron.site  
  
CMD /usr/bin/shiny-server  
  
# docker build -t makaho/shiny-server .  
# docker run -it --rm -p 3838:3838 -v E:\data\docker\shiny\App\:/srv/shiny-
server/app makaho/shiny-server /bin/bash  
# export R_MAX_NUM_DLLS=200  
# in /etc/R/Renviron.site  
# must be <614  
# preserve_logs true;  

