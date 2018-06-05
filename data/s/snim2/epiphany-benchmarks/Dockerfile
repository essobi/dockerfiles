FROM snim2/parallella-devenv  
  
MAINTAINER Sarah Mount <s.mount@wlv.ac.uk>  
  
WORKDIR /home/dev  
  
COPY docker-update.sh /home/dev/docker-update.sh  
  
RUN sh ./docker-update.sh \  
&& rm docker-update.sh  
  
WORKDIR /home/dev/working/epiphany-benchmarks  
  
CMD ["bash"]  

