FROM r-base:latest  
  
MAINTAINER Vanessa Sochat "vsochat@stanford.edu"  
RUN apt-get update && apt-get install -y \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev  
  
# Download and install libssl  
RUN wget https://www.openssl.org/source/openssl-1.0.1t.tar.gz  
RUN tar -xzvf openssl-1.0.1t.tar.gz  
RUN cd openssl-1.0.1t && ./config && make && make install  
RUN cd ..  
RUN rm openssl-1.0.1t.tar.gz  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
RUN R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages('shinyAce')"  
RUN R -e "install.packages('rpivotTable')"  
RUN R -e "install.packages('readxl')"  
RUN R -e "install.packages('tabplot')"  
RUN R -e "install.packages('ggplot2')"  
RUN R -e "install.packages('randomForestSRC')"  
RUN R -e "install.packages('brew')"  
  
RUN mkdir code  
ADD . /code/  
ADD ./shiny-server.sh /usr/bin/shiny-server.sh  
ADD ./raps /srv/shiny-server  
  
RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
EXPOSE 3838  
CMD ["/usr/bin/shiny-server.sh"]  

