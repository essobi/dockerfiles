FROM colebrokamp/r-base  
  
MAINTAINER "Cole Brokamp" cole.brokamp@gmail.com  
  
RUN R -e "install.packages('shiny')"  
  
RUN apt-get update && apt-get install -y \  
gdebi-core \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download and install latest version of shiny server  
RUN wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb  
  
# expose port to access app  
EXPOSE 3838  

