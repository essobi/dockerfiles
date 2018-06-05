FROM rocker/hadleyverse  
  
MAINTAINER kx.it4poster@gmail.com  
  
RUN sudo apt-get -y update && sudo apt-get install -y libgdal-dev libproj-dev  
  
COPY *.R /home/rstudio/  
  
EXPOSE 6311  
RUN mkdir /home/rstudio/workspace && chmod 775 /home/rstudio/workspace  
RUN Rscript /home/rstudio/setupLibs.R  

