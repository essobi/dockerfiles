FROM ubuntu  
MAINTAINER Haydn Dufrene <haydn.dufrene@affirm.com>  
  
ADD dependencies.sh /  
RUN /dependencies.sh  
  
ENTRYPOINT ["/usr/local/bin/moto_server"]  
CMD ["--help"]  

