FROM earthlab/r-spatial-aws  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libcairo2-dev \  
libcurl4-openssl-dev \  
libv8-3.14-dev \  
libxml2-dev  
  
RUN R -e "install.packages('fasterize',dependencies=TRUE,
repos='http://cran.rstudio.com/')" \  
RUN R -e "install.packages('ggmap',dependencies=TRUE,
repos='http://cran.rstudio.com/')" \  
RUN R -e "install.packages('lwgeom',dependencies=TRUE,
repos='http://cran.rstudio.com/')" \  
RUN R -e "install.packages('lme4',dependencies=TRUE,
repos='http://cran.rstudio.com/')" \  
RUN R -e "install.packages('nabor',dependencies=TRUE,
repos='http://cran.rstudio.com/')" \  
RUN R -e "install.packages('tabularaster',dependencies=TRUE,
repos='http://cran.rstudio.com/')" \  
RUN R -e "install.packages('velox',dependencies=TRUE,
repos='http://cran.rstudio.com/')" \  
  
EXPOSE 8787  
  
CMD ["/init"]  

