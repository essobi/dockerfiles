FROM rocker/r-base  
MAINTAINER Jeff Allen <docker@trestletech.com>  
  
RUN useradd plumber \  
&& mkdir /home/plumber \  
&& chown plumber:plumber /home/plumber \  
&& addgroup plumber staff \  
&& mkdir /home/plumber/data \  
&& chown -R plumber /home/plumber/data  
  
RUN apt-get update -qq && apt-get install -y \  
git-core \  
libssl-dev \  
libcurl4-gnutls-dev  
  
RUN R -e 'install.packages(c("devtools"))'\  
&& R -e 'devtools::install_github("trestletech/plumber")' \  
&& R -e "install.packages('fst', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('stringi', repos='https://cran.r-project.org/')"  
VOLUME /home/plumber  
EXPOSE 8000  
CMD ["R", "-e", "setwd('/home/plumber'); r <\- plumber::plumb('api.R');
r$run(host='0.0.0.0', port=8000)"]  
  

