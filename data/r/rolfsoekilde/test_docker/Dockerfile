FROM rocker/hadleyverse:latest  
  
RUN git clone https://github.com/rolfsoekilde/test_docker.git  
WORKDIR test_docker  
RUN R -e "rmarkdown::render('produces_the_sample_rmarkdown.Rmd')"

