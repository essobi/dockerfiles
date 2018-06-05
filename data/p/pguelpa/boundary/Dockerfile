# Dockerfile for Boundary agent  
FROM debian:jessie  
  
MAINTAINER Paul Guelpa  
  
# You need to specify your install token  
# ENV APICREDS <OrganizationID>:<API Key>  
# You can optionally add any environment variables you want to use in the
install script  
# ENV PROVISIONHOSTNAME <gopher>  
ADD ./setup_meter.sh /tmp/setup_meter.sh  
  
ONBUILD ADD ./env /tmp/bprobe-install-env  
ONBUILD RUN . /tmp/bprobe-install-env && /tmp/setup_meter.sh -s  
ONBUILD RUN rm /tmp/bprobe-install-env /tmp/setup_meter.sh  
  
CMD /usr/bin/bprobe -I bprobe  

