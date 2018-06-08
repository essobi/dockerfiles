FROM ubuntu:xenial-20160818  
ENV container=docker  
  
ADD configure-systemd /tmp/  
RUN /tmp/configure-systemd  
  
ENTRYPOINT ["/lib/systemd/systemd"]  

