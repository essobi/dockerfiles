FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
# install rgl dependencies  
RUN apt-get update && apt-get install -y r-cran-rgl libglu1-mesa-dev
freeglut3-dev mesa-common-dev  
  
# install R packages (knitr etc)  
COPY install.R /tmp/  
RUN Rscript --no-save --no-restore /tmp/install.R && \  
rm -f /tmp/install.R  
  
# pyHGVS 0.9.4  
RUN cd /tmp && \  
git clone https://github.com/counsyl/hgvs.git && \  
cd hgvs && git checkout aebe5bd9683f4b5937fd653ce4b13fcd4f3ebb10 && \  
python setup.py install && \  
rm -rf /tmp/*  
  
CMD ["/bin/bash"]  

