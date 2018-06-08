FROM rocker/tidyverse:latest  
  
MAINTAINER MR <mr@m.org>  
  
#copy local dataset and .rmd file to work directory in Rstudio server  
COPY /melanoma_clin.csv /repro/  
COPY /repro_research.rmd /repro/  
  
# System dependencies for required R packages  
RUN rm -f /var/lib/dpkg/available \  
&& rm -rf /var/cache/apt/* \  
&& apt-get update -qq \  
&& apt-get install -y \--no-install-recommends \  
ca-certificates \  
libssl-dev \  
libcurl4-openssl-dev \  
libxml2-dev \  
git  
  
# TeXLive + inconsolata fonts from rocker/hadleyverse  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends \  
aspell \  
aspell-en \  
ghostscript \  
imagemagick \  
lmodern \  
texlive-fonts-recommended \  
texlive-humanities \  
texlive-latex-extra \  
texinfo \  
&& apt-get clean \  
&& cd /usr/share/texlive/texmf-dist \  
&& wget http://mirrors.ctan.org/install/fonts/inconsolata.tds.zip \  
&& unzip inconsolata.tds.zip \  
&& rm inconsolata.tds.zip \  
&& echo "Map zi4.map" >> /usr/share/texlive/texmf-dist/web2c/updmap.cfg \  
&& mktexlsr \  
&& updmap-sys  
  
#install packages needed for this .rmd file  
RUN Rscript -e
"install.packages(c('devtools','knitr','rmarkdown','shiny','RCurl', \  
'survival','ggplot2','rms','survplot','CPE','survminer','pander','plyr', \  
'tableone'), repos = 'https://cran.rstudio.com')"  
  
#allow read/write access to work directory  
RUN chmod -R 777 /repro/  
  
RUN mkdir /repro/  
WORKDIR /repro/  

