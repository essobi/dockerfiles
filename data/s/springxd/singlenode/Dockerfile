FROM springxd/base  
MAINTAINER Eric Bottard  
  
RUN mkdir -p /tmp/xd/output  
RUN mkdir -p /tmp/xd/input  
RUN chown springxd /tmp/xd/output  
RUN chown springxd /tmp/xd/input  
  
CMD ["xd/bin/xd-singlenode"]  
EXPOSE 9393  

