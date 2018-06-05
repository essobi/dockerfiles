FROM consol/tomcat-8.0:8.0.9  
MAINTAINER CI <rt.ci@readytalk.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:/usr/lib/x86_64-linux-gnu/  
  
RUN apt-get update  
RUN apt-get install -y libtcnative-1  
  
CMD ["opt/tomcat/bin/catalina.sh", "run"]

