# docker build --rm -t r-ibeb .  
FROM lipcomputing/rbase  
  
RUN apt-get -y install libcairo2-dev libxt-dev openjdk-8-jdk openjdk-8-jdk-
headless  
ADD installpackages.R /home/installpackages.R  
RUN R CMD javareconf  
RUN R CMD BATCH /home/installpackages.R  

