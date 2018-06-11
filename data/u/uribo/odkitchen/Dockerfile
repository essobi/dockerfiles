FROM rocker/geospatial:3.5.0  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
fonts-ipafont-gothic \  
libpoppler-cpp-dev  
# fonts-ipafont-mincho  
  
RUN install2.r \  
config drake estatapi ggforce here hrbrthemes \  
jpmesh jpndistrict liftr naniar pdftools skimr \  
usethis rlang  
  
RUN installGithub.r uribo/odkitchen  

