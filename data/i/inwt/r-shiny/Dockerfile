FROM inwt/r-batch:3.4.3  
EXPOSE 3838  
RUN install2.r \  
htmlwidgets \  
DT \  
shiny \  
shinydashboard \  
shinyjs \  
shinythemes \  
plotly  
  
# We don't use array syntax because we want to use the ENV varialbe  
# PKG is expected to be configured in the Dockerfile of the app.  
CMD Rscript -e "library(shiny);$PKG::startApplication()" || main  

