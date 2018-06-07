FROM jrnold/rstan:latest  
MAINTAINER Patrick Sadil psadil@gmail.com  
  
# Install 'extras'  
RUN install2.r --error --deps TRUE \  
brms \  
drake  
  
RUN Rscript -e "devtools::install_github('mjskay/tidybayes'); "  

