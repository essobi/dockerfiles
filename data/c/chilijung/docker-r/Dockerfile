FROM bradrydzewski/base  
  
WORKDIR /home/ubuntu  
USER ubuntu  
  
RUN echo 'deb http://cran.cnr.Berkeley.edu/bin/linux/ubuntu precise/' | sudo
tee -a /etc/apt/sources.list && \  
sudo apt-get update && \  
sudo apt-get install r-base && sudo apt-get install r-base-dev  

