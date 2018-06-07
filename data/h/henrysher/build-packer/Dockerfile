FROM iwsaas/centos  
MAINTAINER Henry Huang <henry.s.huang@gmail.com>  
  
RUN yum clean all && yum install mercurial git go gcc bzr make python-pip
python-devel zip -y  
RUN mkdir -p /root/go  
  
ENV GOPATH=/root/go  
ENV PATH=$PATH:/root/go/bin  
COPY build_packer.sh /  
RUN chmod +x -v /build_packer.sh  
ENTRYPOINT ["/build_packer.sh"]  

