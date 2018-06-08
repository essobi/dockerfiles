FROM alpine:edge  
MAINTAINER lauwarm <lauwarm@mailbox.org>  
  
# add testing repository  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
# update the default application repository source list and install needed
packages  
RUN apk update && \  
apk add livestreamer  
  
# set workdir  
WORKDIR /home  
  
# download livestream-recorder.sh from gist  
ADD
https://gist.githubusercontent.com/lauwarm/b39f804c32a938015840/raw/48da22184b9c00bf31cd247b80fca2bb21610cc4/livestream-
recorder.sh /home  
  
# alter permission  
CMD ["chmod", "+x", "livestream-recorder.sh"]  
  
# start the script to record livestreams  
CMD ["./livestream-recorder.sh"]  

