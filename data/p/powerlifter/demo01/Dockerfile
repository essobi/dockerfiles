FROM powerlifter/ubuntugl  
  
MAINTAINER PowerlifterDevOps  
  
RUN mkdir /docker && mkdir /docker/demo01 && mkdir /docker/demo01/lib && mkdir
/docker/demo01/bin && mkdir /docker/demo01/media  
  
COPY lib /docker/demo01/lib/  
  
COPY bin /docker/demo01/bin/  
  
COPY media /docker/demo01/media  
  
CMD export LD_LIBRARY_PATH=/docker/demo01/lib && ./docker/demo01/bin/demo01  

