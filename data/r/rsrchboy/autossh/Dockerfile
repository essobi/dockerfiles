# Teensy autossh tunnel maintenance  
#  
# You should do a bind-mount to get ssh configuration, public-keys, etc, into  
# the running container.  
#  
# -v dotssh:/root/.ssh:ro  
FROM alpine:3.5  
MAINTAINER Chris Weyl <cweyl@alumni.drew.edu>  
  
RUN apk update && \  
apk add autossh && \  
rm -r /var/cache/  
  
ENTRYPOINT [ "autossh", "-gN" ]  

