FROM dugong/dugong:cmd  
MAINTAINER Fabiano Menegidio  
  
RUN /headless/.conda2/bin/conda install -c bioconda antismash prokka \  
&& git clone https://github.com/LaBiOS/PanX.git $HOME/data/xylella  
  
WORKDIR $HOME/data/xylella  

