FROM debian  
MAINTAINER zimbatm <zimbatm@zimbatm.com>  
  
# Storage  
VOLUME ["/data"]  
  
# Make & install  
ADD build.sh /root/build.sh  
RUN sh /root/build.sh  
  
# Config  
EXPOSE 80  
ENV USER root  
ENV HOME /data  
# TODO: other options ?  
# Run  
ENTRYPOINT ["/bin/camlistored", "-listen", ":80"]  

