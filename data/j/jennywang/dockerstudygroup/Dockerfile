# select the base image to build upon  
FROM ubuntu:16.04  
# Leave a bread crumb in case people need help  
MAINTAINER Jenny Wang "jwang@transparent.com"  
# cannot be overridden at container launch time  
ENTRYPOINT ["/bin/cat"]  
  
# can be overriden at container launch time  
CMD ["/opt/local.txt"]  
  
# copy a local file into the container  
ADD local.txt /opt/local.txt  

