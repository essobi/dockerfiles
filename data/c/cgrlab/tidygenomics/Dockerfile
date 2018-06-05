FROM cgrlab/tidyverse  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends git libfftw3-dev libtiff5-dev  
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite()'  
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R");
biocLite("GenomicAlignments")'  
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R");
biocLite("EBImage")'  
RUN Rscript -e 'require(devtools); devtools::install_github("wch/webshot");
require(webshot); webshot::install_phantomjs()'  
RUN Rscript -e 'require(devtools);
devtools::install_github("hadley/dplyr@v0.5.0")'  
RUN Rscript -e 'install.packages("tidygenomics")'  
RUN Rscript -e 'require(tidyverse); sessionInfo()'  

