FROM jvera/base-extras:latest  
  
LABEL maintainer "vera.josemanuel@gmail.com"  
  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R")' -e
'biocLite("pcaMethods")'  
  
ADD check_installs.R /tmp/check_installs.R  
  
RUN Rscript /tmp/check_installs.R  
  
RUN rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
# scanstatistics \  
# styler \  
# stm \  

