FROM rocker/geospatial:latest  
  
# install R packages  
# verify that they are not already presents before adding them  
RUN install2.r --error corrplot ggpubr psy MatchIt tableone pROC cobalt icd \  
DBI MonetDBLite ggmap fmsb survminer optmatch plotly profvis formula.tools \  
  
# and those from github  
&& Rscript -e 'devtools::install_github("IM-APHP/pmeasyr")' \  
&& Rscript -e 'devtools::install_github("AdrienLeGuillou/descriptor")'  
# copy rstudio server user settings  
COPY user-settings /home/rstudio/  
  
RUN mkdir -p /home/rstudio/.rstudio/monitored/user-settings /home/rstudio/work
\  
&& mv /home/rstudio/user-settings /home/rstudio/.rstudio/monitored/user-
settings/ \  
&& chown -R rstudio:rstudio /home/rstudio  

