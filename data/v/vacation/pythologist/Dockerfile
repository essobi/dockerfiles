FROM jupyter/r-notebook  
RUN git clone https://github.com/gusef/IrisSpatialFeatures.git  
RUN Rscript -e
'source("https://bioconductor.org/biocLite.R");biocLite("BiocInstaller")'  
RUN Rscript -e
"install.packages(c('SpatialTools','gplots','spatstat','tiff','data.table','matrixStats'),repos
= 'http://cran.us.r-project.org')"  
RUN Rscript -e 'devtools::install_local("IrisSpatialFeatures")'  
RUN rm -r IrisSpatialFeatures  
RUN Rscript -e "install.packages('tidyverse',repos =
'http://cran.us.r-project.org')"  
RUN pip install pythologist==0.1.7  

