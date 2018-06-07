FROM alpine:3.4  
MAINTAINER Emory Merryman emory.merryman@gmail.com  
COPY run.sh /opt/docker/  
RUN ["/bin/sh", "/opt/docker/run.sh"]  
ENV PATH="/root/bin:${PATH}"  
ENTRYPOINT ["/bin/sh"]  
CMD []  
  

