FROM r-base:latest  
  
RUN R -e "install.packages('Rserve', repos='http://cran.r-project.org')"  
RUN R -e "source('https://bioconductor.org/biocLite.R'); biocLite('snpStats')"  
RUN R -e "install.packages('data.table')"  
RUN R -e "install.packages('rjson')"  
ENV ROOT /usr/share/rserve/config/  
  
EXPOSE 6311  

