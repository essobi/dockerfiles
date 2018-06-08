FROM fabarca/ocpu-rstudio-spatial  
  
RUN Rscript -e "install.packages(c('plumber'),
repos='https://cloud.r-project.org/')"  
  
EXPOSE 8000  
ENTRYPOINT ["R", "-e", "pr <\- plumber::plumb(commandArgs()[4]);
pr$run(host='0.0.0.0', port=8000)"]  
  
CMD ["/usr/local/lib/R/site-library/plumber/examples/04-mean-sum/plumber.R"]  
  

