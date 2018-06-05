FROM debian:wheezy  
MAINTAINER Teezily "dev@teezily.com"  
ADD build /build  
  
RUN /build/prepare.sh && \  
/build/install.sh && \  
/build/cleanup.sh  
  
EXPOSE 11300  
CMD ["/usr/bin/beanstalkd", "-p", "11300"]  

