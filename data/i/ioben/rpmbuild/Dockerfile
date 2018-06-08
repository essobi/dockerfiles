FROM centos:7  
MAINTAINER Ben "ben@ros.io"  
  
ENV USER root  
ENV GOVERSION 1.6.2  
  
ADD build/ /tmp/build/  
RUN bash /tmp/build/setup-env.sh && \  
bash /tmp/build/install-go.sh && \  
rm -rf /tmp/build  

