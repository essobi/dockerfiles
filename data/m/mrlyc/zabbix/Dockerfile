FROM debian:stretch  
  
MAINTAINER lyc <imyikong@gmail.com>  
  
ADD build.sh /build.sh  
ADD entry.sh /entry.sh  
ENV DOCKER_DEBUG 0  
ENV NEEDAUTH true  
ENV USERNAME mrlyc  
ENV PASSWORD pass  
ENV TASKDB ""  
ENV PROJECTDB ""  
ENV RESULTDB ""  
ENV MESSAGEQ ""  
ENV LANG C.UTF-8  
ENV LANG C.UTF-8  
EXPOSE 5000  
WORKDIR ["/opt/pyspider"]  
RUN ["/build.sh"]  
  
VOLUME ["/opt/pyspider"]  
  
ENTRYPOINT ["/entry.sh"]  
CMD ["-c", "pyspider.json"]  

