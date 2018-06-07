#  
# Dynamic Software Update Dockerfile  
#  
# Pull base image  
FROM samirabloom/docker-go  
  
# Maintainer details  
MAINTAINER Samira Rabbanian "samira.rabanian@gmail.com"  
# Setup correct GOPATH  
ENV GOPATH /home/goworld  
  
# install dependencies  
RUN git clone https://github.com/samirabloom/doxy && \  
cd doxy && \  
make  
  
VOLUME /config  
  
# define default command  
CMD ["doxy", "-logLevel", "INFO", "-configFile", "/config/config.json"]

