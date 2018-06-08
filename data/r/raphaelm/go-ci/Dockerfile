FROM golang:1.5-wheezy  
  
MAINTAINER Raphael Michel  
  
RUN apt-get update && apt-get install -y wget locales  
  
RUN locale-gen  
RUN update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

