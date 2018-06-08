from robbyjo/r-mkl-bioconductor:3.4.1  
MAINTAINER tim majarian (tmajaria@broadinstitute.org)  
  
RUN apt-get update  
RUN apt-get -y install git  
  
RUN echo 'source("https://bioconductor.org/biocLite.R")' > install.R && \  
echo "biocLite(c('SeqArray'), dependencies=TRUE, clean=TRUE, INSTALL_opts='--
no-docs --no-demo --byte-compile');" >> install.R && \  
echo "biocLite(ask=FALSE, clean=TRUE, INSTALL_opts='--no-docs --no-demo
--byte-compile');" >> install.R && \  
Rscript --vanilla install.R && \  
rm install.R  
  
RUN git clone https://github.com/manning-lab/vcfToGds.git && cd ./vcfToGds &&
git pull origin master

