# Beaker (Jupyter/iPython/Knitr alternative) with extra tools  
#  
# VERSION 1.0.0  
FROM beakernotebook/beaker  
MAINTAINER Bruno Vieira <mail@bmpvieira.com>  
  
LABEL Description="Latest Beaker image with a few extra tools" Version="1.0.0"  
  
RUN apt-get install -y libfftw3-dev libtiff4-dev # Required by EBImage (ggtree
phylopic dep)  
RUN R -e ' \  
install.packages("phytools", repos="http://cran.us.r-project.org") ;\  
source("https://bioconductor.org/biocLite.R") ;\  
biocLite("ggtree") ;\  
biocLite("EBImage") ;\  
'  

