FROM crukcibioinformatics/shiny-base  
  
RUN R -e 'install.packages("RSQLite", repos = "https://cloud.r-project.org")'  
RUN R -e 'install.packages("dbplyr", repos = "https://cloud.r-project.org")'  
#RUN R -e 'install.packages("DT", repos = "https://cloud.r-project.org")'  
# install latest development version of DT from github  
# stable release v0.2 has ajax error issue
(https://github.com/rstudio/DT/issues/266)  
# note that one of the dependencies of the devtools package (httr) requires
curl and openssl  
RUN R -e 'install.packages("devtools", repos = "https://cloud.r-project.org")'  
RUN R -e 'devtools::install_github("rstudio/DT")'  
  
RUN R -e 'install.packages("gridExtra", repos =
"https://cloud.r-project.org")'  
RUN R -e 'install.packages("ggthemes", repos = "https://cloud.r-project.org")'  
RUN R -e 'install.packages("GGally", repos = "https://cloud.r-project.org")'  
RUN R -e 'install.packages("gplots", repos = "https://cloud.r-project.org")'  
RUN R -e 'install.packages("heatmap.plus", repos =
"https://cloud.r-project.org")'  
RUN R -e 'install.packages("party", repos = "https://cloud.r-project.org")'  
  
RUN R -e 'source("https://bioconductor.org/biocLite.R"); biocLite("Biobase")'  
RUN R -e 'source("https://bioconductor.org/biocLite.R");
biocLite("preprocessCore")'  
RUN R -e 'source("https://bioconductor.org/biocLite.R");
biocLite("AnnotationDbi")'  
RUN R -e 'source("https://bioconductor.org/biocLite.R"); biocLite("impute")'  
RUN R -e 'source("https://bioconductor.org/biocLite.R");
biocLite("org.Hs.eg.db")'  
RUN R -e 'source("https://bioconductor.org/biocLite.R"); biocLite("GO.db")'  
  
RUN R -e 'install.packages("WGCNA", repos = "https://cloud.r-project.org")'  
  
RUN mkdir /srv/shiny-server/camcAPP  
RUN mkdir /srv/shiny-server/camcAPP/data  
RUN mkdir /srv/shiny-server/camcAPP/www  
  
RUN chmod -R ugo+rx /srv/shiny-server/camcAPP  
  
COPY server.R /srv/shiny-server/camcAPP/  
COPY UI.R /srv/shiny-server/camcAPP/  
COPY google-analytics.js /srv/shiny-server/camcAPP/  
COPY data/curated.genes.txt /srv/shiny-server/camcAPP/data/  
COPY www/* /srv/shiny-server/camcAPP/www/  
  
RUN chmod -R ugo+r /srv/shiny-server/camcAPP  
  

