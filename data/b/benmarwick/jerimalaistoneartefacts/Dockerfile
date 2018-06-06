FROM rocker/hadleyverse  
  
MAINTAINER Ben Marwick <benmarwick@gmail.com>  
  
## Install software dependencies  
RUN apt-get update \  
&& apt-get install -y \  
r-cran-rjags \  
r-cran-coda \  
r-cran-vcd \  
## && RUN Rscript -e 'install.packages("runjags")' \ ## not available as
r-cran-runjags  
  
&& install2.r --error --deps TRUE \  
runjags \  
  
&& rm -rf /tmp/downloaded_packages/ \  
  
&& installGithub.r --deps TRUE \  
kenkellner/jagsUI \  
mikemeredith/BEST \  
yihui/printr \  
ropensci/dependencies \  
ropensci/git2r \  
benmarwick/Pleistocene-aged-stone-artefacts-from-Jerimalai--East-Timor  
  
## get full copy of my package & compendium  
RUN git clone https://github.com/benmarwick/Pleistocene-aged-stone-artefacts-
from-Jerimalai--East-Timor.git \  
  
## make it writable  
&& chmod 777 -R Pleistocene-aged-stone-artefacts-from-Jerimalai--East-Timor \  
  
## generate HTML files from Rmd (~30 min)  
&& Rscript -e 'rmarkdown::render("/Pleistocene-aged-stone-artefacts-from-
Jerimalai--East-Timor/manuscript/Bayesian_Motivations.Rmd")' \  
  
&& Rscript -e 'rmarkdown::render("/Pleistocene-aged-stone-artefacts-from-
Jerimalai--East-Timor/manuscript/lithic_data_analysis_both_squares.Rmd")'  
  
  
  
# How to make the image:  
# docker build -t benmarwick/jerimalaistoneartefacts --no-cache
https://raw.githubusercontent.com/benmarwick/Pleistocene-aged-stone-artefacts-
from-Jerimalai--East-Timor/master/docker/Dockerfile  
# An 'automated build' on the docker hub  

