FROM marlinl/alpine-nodejs:latest  
  
MAINTAINER malin3369@gmail.com  
  
# install python for mqtt borker  
RUN apk update && \  
apk add \--no-cache \  
python make gcc g++ zeromq-dev  
  
  
EXPOSE 1883  

