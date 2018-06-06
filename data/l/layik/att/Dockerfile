FROM robinlovelace/geocompr  
  
RUN R -e 'install.packages(c("devtools"))'  
RUN R -e 'devtools::install_github("trestletech/plumber")'  
  
ADD . /app  
  
EXPOSE 8000  
ENTRYPOINT ["R", "-e", "setwd('/app/static');
plumber::plumb('../server/plumber.R')$run(host='0.0.0.0',port=8000)"]

