FROM trestletech/plumber  
MAINTAINER Troy James Palanca <tjpalanca@uber.com>  
  
RUN apt-get update -qq && apt-get install -y \  
git-core \  
libssl-dev \  
libcurl4-gnutls-dev  
  
RUN R -e 'install.packages(c("httr", "magrittr", "jsonlite", "stringr",
"purrr"))'  
  
CMD ["/app/plumber.R"]  

