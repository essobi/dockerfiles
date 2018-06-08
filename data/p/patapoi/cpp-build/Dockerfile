FROM ubuntu:zesty  
  
COPY setup-common.sh /usr/local/bin/  
COPY setup-folly.sh /usr/local/bin/  
RUN /bin/bash /usr/local/bin/setup-common.sh  
RUN /bin/bash /usr/local/bin/setup-folly.sh  
  
USER docker  
VOLUME /home/docker  
WORKDIR /home/docker  

