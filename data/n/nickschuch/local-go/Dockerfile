FROM ubuntu:14.04  
MAINTAINER Nick Schuch <nick@previousnext.com.au>  
  
ADD ./scripts/base.sh /root/base.sh  
ADD ./scripts/provision.sh /root/provision.sh  
RUN chmod a+x /root/base.sh  
RUN chmod a+x /root/provision.sh  
  
RUN /root/base.sh  
RUN /root/provision.sh  
  
ENV PATH /opt/golang/bin:/usr/local/go/bin:$PATH  
ENV GOPATH /opt/golang  
  
CMD ["/bin/bash"]  

