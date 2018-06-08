FROM jangorecki/r-base-dev:latest  
MAINTAINER Mike Birdgeneau <mike.birdgeneau@gmail.com>  
  
COPY requirements.R requirements.R  
RUN apt-get update  
  
RUN apt-get install -y --no-install-recommends \  
libgdal-dev \  
libproj-dev \  
python-pip \  
python-setuptools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget
https://github.com/jgm/pandoc/releases/download/1.19.1/pandoc-1.19.1-1-amd64.deb  
RUN dpkg -i pandoc-1.19.1-1-amd64.deb  
RUN Rscript -e 'source("requirements.R");
install.packages(pkg_list,repos="https://cran.rstudio.com/")'  
RUN Rscript -e 'install.packages("devtools");
devtools::install_github("Rdatatable/data.table")'  
RUN apt-get -y remove libgdal-dev libproj-dev && apt-get -y autoremove  
  
RUN pip install awscli  
CMD ["R"]  

