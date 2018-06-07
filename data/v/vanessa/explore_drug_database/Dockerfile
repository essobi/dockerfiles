FROM rocker/r-base  
MAINTAINER vsochat@stanford.edu  
  
# Install curl, ssl, and xml libraries  
RUN apt-get update && apt-get install -y libcurl4-gnutls-dev \  
libssl-dev \  
libxml2-dev  
  
# Install pandoc  
RUN wget
https://github.com/jgm/pandoc/releases/download/1.19.2/pandoc-1.19.2-1-amd64.deb  
RUN dpkg -i pandoc-1.19.2-1-amd64.deb  
  
# Install dependency packages  
RUN R -e 'install.packages("rvest", repos = "http://cran.us.r-project.org")'  
RUN R -e 'install.packages("tidyr", repos = "http://cran.us.r-project.org")'  
RUN R -e 'install.packages("dplyr", repos = "http://cran.us.r-project.org")'  
RUN R -e 'install.packages("ggplot2", repos = "http://cran.us.r-project.org")'  
RUN R -e 'install.packages("rmarkdown", repos =
"http://cran.us.r-project.org")'  
RUN R -e 'install.packages("XML", repos = "http://cran.us.r-project.org")'  
RUN R -e 'install.packages("readr", repos = "http://cran.us.r-project.org")'  
RUN R -e 'install.packages("DT", repos = "http://cran.us.r-project.org")'  
RUN R -e 'install.packages("wordcloud2", repos =
"http://cran.us.r-project.org")'  
  
# Add a simple nginx web server to serve Rmd notebooks  
RUN apt-get install -y nginx python  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
RUN mkdir /code  
RUN mkdir /data  
ADD . /code  
RUN chmod u+x /code/*  
WORKDIR /code  
CMD /code/run.sh  

