# Alpine linux docker image  
FROM alpine:latest  
  
MAINTAINER Mario Cho <hephaex@gmail.com>  
  
# Install packages.  
RUN \  
apk update && \  
apk upgrade && \  
apk --update add bash && \  
rm -rf /var/cache/apk/*  
  
# Set the default command.  
CMD ["/bin/bash"]

