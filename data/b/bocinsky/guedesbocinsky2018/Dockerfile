# get the base image  
FROM bocinsky/bocin_base:latest  
  
# required  
MAINTAINER Kyle Bocinsky <bocinsky@gmail.com>  
  
COPY . /guedesbocinsky2018  
  
# Install dev version of devtools to facilitate installing from "remotes"
field in DESCRIPTION  
RUN r -e 'devtools::install_cran("remotes")'  
  
# build this compendium package  
RUN r -e 'devtools::install("/guedesbocinsky2018", dependencies = TRUE,
upgrade_dependencies = FALSE)'  
  
# install the remotes  
RUN r -e 'remotes::install_local("/guedesbocinsky2018")'  
  
# Check the package  
RUN r -e 'devtools::check("/guedesbocinsky2018", vignettes = FALSE, args = "--
no-vignettes")'  
  
# render the analysis  
# && r -e
"rmarkdown::render('/guedesbocinsky2018/vignettes/guedesbocinsky2018.Rmd')"  

