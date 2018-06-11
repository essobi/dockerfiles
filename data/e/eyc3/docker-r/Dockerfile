FROM rocker/geospatial:3.4.2  
  
WORKDIR /build  
  
## install r package os dependencies  
RUN apt-get update \  
&& apt-get install -y \  
libudunits2-dev \  
# rmapshaper dependencies  
libjq-dev \  
libprotobuf-dev \  
protobuf-compiler  
  
## install rstan with personal Makevars file  
## workaround for issue: https://github.com/stan-dev/rstan/issues/441  
## this should be fixed with the rstan 2.17 release  
ADD create_makevars.R /build  
RUN R -e "source('create_makevars.R')"  
## install additional r packages  
RUN install2.r --error \  
\--deps TRUE \  
shinydashboard \  
plotly \  
prophet \  
leaflet \  
GWmodel \  
readbulk \  
pool \  
rmapshaper  

