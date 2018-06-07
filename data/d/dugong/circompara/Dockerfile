FROM dugong/dugong:icewm  
MAINTAINER Fabiano Menegidio  
  
RUN /headless/.conda2/bin/conda install numpy scipy bioconductor-deseq2 pandoc
r-bh r-optparse r-scales r-reshape2 \  
r-ggplot2 r-rmarkdown r-knitr && /headless/.conda2/bin/conda clean -tipsy \  
&& git clone http://github.com/fabianomenegidio/circompara $HOME/CirComPara \  
&& cd $HOME/CirComPara \  
&& chmod -R 755 $HOME/CirComPara/tools/*  
  
WORKDIR $HOME/CirComPara  

