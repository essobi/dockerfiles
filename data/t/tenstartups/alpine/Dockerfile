#  
# Alpine linux docker image  
#  
# A minimal base image based on Alpine Linux with useful packages and tools.  
#  
# http://github.com/tenstartups/alpine-docker  
#  
FROM alpine:latest  
  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
  
# Set environment variables.  
ENV \  
TERM=xterm-color  
  
# Install packages.  
RUN \  
apk --update add bash coreutils curl nano procps rsync tar wget && \  
rm -rf /var/cache/apk/*  
  
# Set the default command.  
CMD ["/bin/bash"]  

