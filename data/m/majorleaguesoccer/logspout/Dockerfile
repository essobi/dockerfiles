FROM flynn/busybox  
MAINTAINER Bryce Kahle <bryce.kahle@mlssoccer.com>  
  
ADD ./stage/logspout /bin/logspout  
  
ENV DOCKER unix:///tmp/docker.sock  
ENV ROUTESPATH /mnt/routes  
VOLUME /mnt/routes  
  
EXPOSE 8000  
ENTRYPOINT ["/bin/logspout"]  
CMD []  

