FROM cannin/r-shiny-server:ubuntu-14.04.4_r-3.2.3_shiny-server-1.4.2.786  
  
COPY inst/scripts/installPackage.R installPackage.R  
RUN R -e 'source("installPackage.R")'  
  
RUN cp -R /usr/local/lib/R/site-library/kircImmuneProject/shinyApp/
/srv/shiny-server/kircImmuneProject/  
# Copy data from data folder  
RUN cp -R /usr/local/lib/R/site-library/kircImmuneProject/extdata/*
/usr/local/lib/R/site-library/kircImmuneProject/shinyApp/www/db  
  
CMD ["shiny-server"]  

