FROM rocker/hadleyverse  
  
RUN install2.r --error \  
-r "https://cran.rstudio.com" \  
-r "http://www.bioconductor.org/packages/release/bioc" \  
rstan \  
loo \  
coda \  
mvtnorm \  
  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
RUN echo "r <\- getOption('repos'); r['rethinking'] <\- 'http://xcelab.net/R';
options(repos = r);" > ~/.Rprofile  
RUN Rscript -e "install.packages('rethinking', type='source')"  
  
## httr authentication uses this port  
EXPOSE 1410  
ENV HTTR_LOCALHOST 0.0.0.0  

