# our R base image  
FROM rocker/tidyverse:3.4.2  
RUN apt-get update && apt-get install -y \  
libjpeg-dev \  
libudunits2-dev \  
libgdal-dev \  
libproj-dev  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# create an R user  
ENV HOME /home/rstudio  
#RUN useradd --create-home --home-dir $HOME user \  
# && chown -R user:user $HOME  
## Needed to have write permissions to the R lib directory  
#RUN sudo usermod -a -G staff user  
RUN echo 'options(repos = list(CRAN =
"https://mran.revolutionanalytics.com/snapshot/2017-11-12/"))' >>
/etc/Rprofile.site  
  
#WORKDIR $HOME  
#USER user  
#RUN mkdir -p $HOME/R/library  
#RUN echo 'R_LIBS=$HOME/R/library' >> ~/.Renviron  
# install packages  
RUN Rscript --slave --no-save --no-restore-history -e 'if (!require("pacman"))
install.packages("pacman");pacman::p_load(aire.zmvm, TimeProjection, dplyr,
ggplot2, ggseas, ggforce, svglite, viridis, lubridate, ggmap, ggthemes,
directlabels)'  
RUN Rscript -e 'install.packages("selectr")'  
RUN Rscript -e 'devtools::install_github("diegovalle/mxmaps")'  
  
# Copy the r program  
RUN mkdir -p $HOME/pollution/output  
COPY emergency.Rmd $HOME/pollution  
COPY *.csv $HOME/pollution/  
COPY *.png $HOME/pollution/  
COPY *.jpg $HOME/pollution/  
COPY pollution_emergency.Rproj $HOME/pollution/  
RUN chown -R rstudio:rstudio /home/rstudio/pollution  
  
# set the command  
#CMD cd pollution && Rscript -e 'library(rmarkdown);
rmarkdown::render("emergency.Rmd", "github_document",
output_dir="output/emergency.html")'  
#CMD /bin/bash

