FROM maxromanovsky/springxd-base:1.3.1  
MAINTAINER Eric Bottard  
MAINTAINER Maksim Ramanouski a.k.a. maxromanovsky  
  
RUN mkdir -p /tmp/xd/output  
RUN mkdir -p /tmp/xd/input  
RUN chown springxd /tmp/xd/output  
RUN chown springxd /tmp/xd/input  
  
CMD ["xd/bin/xd-singlenode"]  
EXPOSE 9393  

