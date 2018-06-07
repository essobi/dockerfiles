FROM rocker/tidyverse:3.4.4  
ENV DATEEXTRACT_VERSION 0.1.0  
COPY dateextract dateextract  
  
RUN \  
export ADD=shiny && bash /etc/cont-init.d/add \  
&& install2.r --error --deps TRUE \  
DT \  
shinydashboard \  
&& R CMD build dateextract \  
&& R CMD INSTALL dateextract_$DATEEXTRACT_VERSION.tar.gz \  
&& rm dateextract_$DATEEXTRACT_VERSION.tar.gz \  
&& mkdir -p /app/dateextractshiny \  
# so that we know which port to expose  
&& echo "local({options(shiny.port = 3838, shiny.host = '0.0.0.0')})" >>
/usr/local/lib/R/etc/Rprofile.site \  
&& apt-get update \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ui.R /app/dateextractshiny  
COPY server.R /app/dateextractshiny  
  
EXPOSE 3838  
CMD ["R", "-e", "shiny::runApp('/app/dateextractshiny')"]  

