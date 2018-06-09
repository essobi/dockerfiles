FROM sunyi00/centos:1.0.0  
RUN yum -y install unzip \  
&& yum -y clean all  
  
RUN cd tmp \  
&& curl -OL https://storage.googleapis.com/golang/go1.6.2.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzf go1.6.2.linux-amd64.tar.gz \  
&& rm -rf go1.6.2.linux-amd64.tar.gz \  
&& echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile  
  
ENV PATH=$PATH:/usr/local/go/bin  
  
RUN mkdir -p /go/src /go/bin && chmod -R 777 /go  
ENV GOPATH /go  
ENV PATH /go/bin:$PATH  
WORKDIR /go  

