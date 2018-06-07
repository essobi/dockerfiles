  
FROM rocker/r-base  
MAINTAINER Jeff Allen <docker@trestletech.com>  
  
RUN apt-get update -qq && apt-get install -y \  
git-core \  
libssl-dev \  
libxml2-dev \  
libcurl4-gnutls-dev \  
libsasl2-dev  
  
RUN R -e 'install.packages(c("devtools", "plyr", "scales", "mongolite"))'  
  
RUN R -e 'devtools::install_github("trestletech/plumber")'  
RUN R -e 'devtools::install_github("jennybc/googlesheets")'  
  
WORKDIR /home/plumb/api/  
COPY . /home/plumb/api/  
  
EXPOSE 8000  
ENTRYPOINT ["R", "-e", "pr <\- plumber::plumb(commandArgs()[4]);
pr$run(host='0.0.0.0', port=8000)"]  
CMD ["/home/plumb/api/plumber.R"]  
  

