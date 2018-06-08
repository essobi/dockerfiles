FROM rocker/shiny  
  
MAINTAINER "Lincoln Mullen" lincoln@lincolnmullen.com  
LABEL Description="A Shiny app to predict gender from first names"  
  
RUN install2.r --error \  
RColorBrewer \  
devtools \  
dplyr \  
dygraphs \  
shinythemes \  
tidyr \  
xts \  
&& installGithub.r \  
ropensci/gender \  
ropensci/genderdata  
  
RUN rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
RUN rm -rf /srv/shiny-server/*  
  
ADD *.R /srv/shiny-server/  
ADD www /srv/shiny-server/www  
  
EXPOSE 3838  
CMD ["/usr/bin/shiny-server.sh"]  

