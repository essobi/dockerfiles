FROM r-base:latest  
  
MAINTAINER Taekyung Yoo "tkyoo@nexon.co.kr"  
  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev \  
r-cran-rmysql \  
fonts-nanum \  
libssl-dev  
  
# Install OpenJDK-8  
RUN apt-get install -y openjdk-8-jdk r-cran-rjava  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
# Download and install shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb && \  
R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cran.rstudio.com/')" && \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/  
  
# Install R Packages  
RUN R -e "install.packages('shiny', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('rJava', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('RJDBC', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('shinythemes', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('shinyBS', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('rmarkdown', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('DT', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('ggplot2', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('ggrepel', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('dplyr', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('tidyr', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('networkD3', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('RColorBrewer', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('tidyverse', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('jsonlite', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('wordcloud', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('gridExtra', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('shinyjs', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('devtools', repos='http://cran.rstudio.com/')" && \  
R -e "install.packages('lubridate', repos='http://cran.rstudio.com/')" && \  
R -e "devtools::install_github(\"rstudio/sparklyr\")" && \  
R CMD javareconf  
  
EXPOSE 3838  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
COPY lib /home/shiny/lib  
  
CMD ["/usr/bin/shiny-server.sh"]  

