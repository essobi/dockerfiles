FROM rocker/tidyverse  
  
RUN apt-get update -qq && apt-get -y --no-install-recommends install \  
texlive-latex-base \  
&& R -e "devtools::install_github('thomasp85/fiery');
devtools::install_github('thomasp85/routr'); install.packages('rcmdcheck')"  

