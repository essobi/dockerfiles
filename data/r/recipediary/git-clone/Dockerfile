FROM ubuntu:14.04.1  
# add script to run  
ADD *.sh /usr/local/bin/  
RUN bash -xe /usr/local/bin/install.sh  
  
WORKDIR /var/workspace  
  
VOLUME /var/workspace  
  
CMD /bin/bash /usr/local/bin/run.sh  
  

