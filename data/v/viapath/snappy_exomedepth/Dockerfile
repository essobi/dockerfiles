FROM viapath/snappy_reporting:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
# install R packages (knitr etc)  
COPY install.R /tmp/  
RUN Rscript --no-save --no-restore /tmp/install.R && \  
rm -f /tmp/install.R  
  
CMD ["/bin/bash"]  

