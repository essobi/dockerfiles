FROM p711/phoenix  
  
MAINTAINER Ron Arts <ron.arts@p711.net>  
  
RUN echo "http://dl-5.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk add --no-cache --update openrc docker bash python && \  
rc-update add docker boot  
  
CMD ["/bin/bash"]  
  

