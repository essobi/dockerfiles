FROM quantumobject/docker-shiny  
  
# libxml2-dev is required for XML, a dependency of quanteda  
RUN apt-get update \  
&& apt-get install -y libxml2-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /srv/shiny-server/* \  
&& mkdir -p /srv/shiny-server/www \  
&& Rscript -e "install.packages('data.table', dependencies=c('Depends',
'Imports', 'LinkingTo'), repos='http://cran.rstudio.com/')" \  
&& Rscript -e "install.packages('doParallel', dependencies=c('Depends',
'Imports', 'LinkingTo'), repos='http://cran.rstudio.com/')" \  
&& Rscript -e "install.packages('quanteda', dependencies=c('Depends',
'Imports', 'LinkingTo'), repos='http://cran.rstudio.com/')" \  
&& Rscript -e "install.packages('shiny', dependencies=c('Depends', 'Imports',
'LinkingTo'), repos='http://cran.rstudio.com/')" \  
&& Rscript -e "install.packages('stringr', dependencies=c('Depends',
'Imports', 'LinkingTo'), repos='http://cran.rstudio.com/')"  
  
COPY app.R predictNext.R tokenizer.R /srv/shiny-server/  
COPY www/* /srv/shiny-server/www/

