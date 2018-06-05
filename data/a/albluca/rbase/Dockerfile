FROM rocker/rstudio  
LABEL maintainer="Luca Albergante <luca.albergante@gmail.com>"  
  
# Install libraries needed by the rRoma package family  
# scater needs XML, which needs libxml2-dev and need to be installed
separatedly  
RUN apt-get update  
RUN apt-get install libxml2-dev  
  
RUN R -e " source('https://bioconductor.org/biocLite.R'); biocLite('scater')"  
RUN R -e " install.packages(c('devtools', 'irlba', 'reshape', 'R.utils',
'readr', 'mice', 'codetools', 'RJSONIO', 'Rtsne'), repos =
'http://cran.us.r-project.org')"  
RUN R -e " install.packages(c('ggplot2', 'gridExtra', 'pheatmap', 'ggsignif',
'colorRamps', 'plotly'), repos = 'http://cran.us.r-project.org')"  
RUN R -e " install.packages(c('shiny', 'shinyFiles'), repos =
'http://cran.us.r-project.org')"  

