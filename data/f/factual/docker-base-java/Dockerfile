FROM boritzio/docker-base  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN apt-get update  
RUN update-ca-certificates -f  
RUN apt-get install -y openjdk-8-jre-headless  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

