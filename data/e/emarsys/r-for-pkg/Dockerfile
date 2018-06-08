FROM rocker/r-ver:3.5.0  
  
RUN apt-get update  
  
RUN apt-get install -y libssl-dev \  
zlib1g-dev \  
libssl-dev \  
libxml2-dev \  
libmariadb2 \  
libmariadb-client-lgpl-dev \  
libpq-dev \  
pandoc \  
pandoc-citeproc \  
qpdf  
  
RUN apt-get install -y libcurl4-openssl-dev  
  
RUN install2.r --error \  
boot \  
cluster \  
class \  
codetools \  
foreign \  
KernSmooth \  
lattice \  
MASS \  
Matrix \  
mgcv \  
nlme \  
nnet \  
rpart \  
spatial \  
survival  
  

