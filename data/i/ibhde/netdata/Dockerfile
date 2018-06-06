FROM debian:stretch-slim  
  
ADD bpo.list /etc/apt/sources.list.d/  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-
install-recommends -y -t stretch-backports netdata  
  
EXPOSE 19999  
ENTRYPOINT ["/usr/sbin/netdata", "-D", "-i 0.0.0.0"]  
CMD ["-s", "/host"]  

