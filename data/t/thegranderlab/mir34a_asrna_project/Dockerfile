FROM rocker/tidyverse:3.4.2  
  
MAINTAINER Jason Serviss <jason.serviss@ki.se>  
  
# System dependencies for required R packages  
RUN rm -f /var/lib/dpkg/available \  
&& rm -rf /var/cache/apt/* \  
&& apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
libssl-dev \  
libcurl4-openssl-dev \  
libxml2-dev \  
git  
  
RUN Rscript -e
"install.packages(c('devtools','knitr','rmarkdown','shiny','RCurl'), repos =
'https://cran.rstudio.com')"  
  
RUN Rscript -e
"source('https://cdn.rawgit.com/road2stat/liftrlib/aa132a2d/install_cran.R');install_cran(c('knitr/1.17','rmarkdown/1.6','printr/0.1','ggthemes/3.4.0','gggenes/0.2.0','extrafont/0.17','scales/0.5.0','gtable/0.2.0','liftr/0.7','rlang/0.1.2','magrittr/1.5','gridExtra/2.3','broom/0.4.3','survival/2.41-3','KMsurv/0.1-5'))"  
  
RUN Rscript -e
"source('https://cdn.rawgit.com/road2stat/liftrlib/aa132a2d/install_remotes.R');install_remotes(c('GranderLab/miR34a_asRNA_project'))"  
  
WORKDIR /home/miR34a_asRNA_project  

