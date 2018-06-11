From rocker/geospatial:latest  
Maintainer "Carson Sievert" cpsievert1@gmail.com  
  
# update/install system dependencies, update R packages  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
libprotobuf-dev protobuf-compiler \  
&& Rscript -e "update.packages(ask=FALSE)"  
  
# Install R packages (doing this one-by-one helps leverage caching)  
RUN R -e "install.packages('shiny')"  
RUN R -e "install.packages('rmarkdown')"  
RUN R -e "install.packages('crosstalk')"  
RUN R -e "install.packages('cranlogs')"  
RUN R -e "install.packages('dplyr')"  
RUN R -e "install.packages('DT')"  
RUN R -e "install.packages('sf')"  
# needed in order for leaflet to respect highlight()  
RUN R -e "remotes::install_github('rstudio/leaflet#346')"  
  
# currently need dev version of ggplot2 to work well with plotly  
RUN R -e "install.packages('remotes')"  
RUN R -e "remotes::install_github('ropensci/plotly')"  
  
# other nice to haves  
RUN R -e "install.packages('GGally')"  
RUN R -e "install.packages('heatmaply')"  
RUN R -e "install.packages('listviewer')"  
RUN R -e "remotes::install_github('hafen/trelliscopejs')"  
RUN R -e "install.packages('gapminder')"  
  
# to have plot_mapbox work out-of-the...box  
RUN echo "Sys.setenv('MAPBOX_TOKEN' =
'pk.eyJ1IjoiY3BzaWV2ZXJ0IiwiYSI6ImNpdGRiOWwwMjAwMHQyem84NG5tcXg5eXIifQ.UJ2VwrJmPW8DB8H2d-wN3g')"
>> /usr/local/lib/R/etc/Rprofile.site  
  
# copy over workshop materials  
COPY slides /home/rstudio  

