# Base Image  
FROM r-base:3.3.2  
# Metadata  
LABEL base.image="r-base:latest"  
LABEL version="3.3.2"  
  
# Maintainer  
MAINTAINER Andrew Wong <nderoo.wong@gmail.com>  
  
# R dependencies  
RUN Rscript -e "install.packages('optparse', dep=TRUE)" && \  
Rscript -e "install.packages('ggplot2', dep=TRUE)" && \  
Rscript -e "install.packages('scales', dep=TRUE)"  
  
ENTRYPOINT ["Rscript"]  
  
CMD ["--help"]  

