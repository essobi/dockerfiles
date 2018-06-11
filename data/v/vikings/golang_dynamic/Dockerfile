FROM centos:7  
MAINTAINER zhangtao<ztao8607@gmail.com>  
  
RUN yum update & \  
yum install -y libffi-devel \  
hg \  
git \  
gcc  
  
# ADD go1.7.linux-amd64.tar.gz /tmp  
RUN cd /tmp ; curl -LO https://storage.googleapis.com/golang/go1.7.linux-
amd64.tar.gz ; \  
tar -C /usr/local -xvzf go1.7.linux-amd64.tar.gz  
# RUN cd /tmp ; tar -C /usr/local -xvzf go1.7.linux-amd64.tar.gz  
RUN mkdir -p /golang/src  
ENV PKG_CONFIG_PATH=/usr/lib64/pkgconfig/  
ENV GOPATH=/golang  
ENV PATH=$PATH:/usr/local/go/bin  
RUN env  
RUN go get bitbucket.org/binet/go-ffi/pkg/ffi  
  
WORKDIR /golang/src  
CMD ["/bin/bash"]  

