FROM uwgac/topmed-master:latest  
RUN apt-get update && apt-get -y install git dstat  
  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e "install.packages('data.table')"  
  
RUN git clone https://github.com/manning-lab/aggregateAssociation.git

