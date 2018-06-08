FROM bioconductor/release_core2  
MAINTAINER Nuno Agostinho <nunodanielagostinho@gmail.com>  
  
RUN apt-get update  
RUN Rscript -e 'install.packages("devtools")'  
RUN Rscript -e 'devtools::install_github("nuno-agostinho/psichomics",
ref="dev")'  

