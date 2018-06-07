# This is the Dockefile to build DToxS  
# Base Docker Image  
FROM r-base  
  
# Maintainer  
MAINTAINER Trevor Meiss "tmeiss@uw.edu"  
# Install required R Packages  
RUN echo 'install.packages(c("matrixStats","gplots","compare"),
dependencies=TRUE)' > /tmp/packages.R  
RUN echo 'source("https://bioconductor.org/biocLite.R")' >> /tmp/packages.R  
RUN echo 'biocLite("locfit")' >> /tmp/packages.R  
RUN echo 'biocLite("edgeR")' >> /tmp/packages.R  
RUN Rscript /tmp/packages.R  
  
ENV HOME /home/user  
WORKDIR $HOME  
  
# Add input directories/files  
ADD Configs/ $HOME/Configs/  
ADD Counts/ $HOME/Counts/  
ADD Params/ $HOME/Params/  
ADD Programs/ $HOME/Programs/  
ADD Results/ $HOME/Results/  
ADD Scripts/ $HOME/Scripts/  
ADD CompareResults/ $HOME/CompareResults/  
  
CMD ["/bin/bash"]  

