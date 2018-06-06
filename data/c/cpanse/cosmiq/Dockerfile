FROM bioconductor/devel_proteomics  
MAINTAINER Christian Panse <cp@fgcz.ethz.ch>  
  
RUN sudo apt-get install git -y  
  
RUN cd /tmp && git clone https://github.com/Bioconductor-mirror/cosmiq.git  
  
RUN echo "source(\"http://bioconductor.org/biocLite.R\"); biocLite(\"cosmiq\",
suppressUpdates=TRUE, ask=FALSE)" | R --no-save  
  
RUN cd /tmp && R CMD build --no-build-vignettes cosmiq \  
#&& R CMD check cosmiq_*.tar.gz \  
&& R CMD INSTALL cosmiq_*.tar.gz \  
&& echo "packageVersion('cosmiq')" | R --no-save  

