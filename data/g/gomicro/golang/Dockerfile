FROM fedora:24  
MAINTAINER Daniel Hess <dan9186@gmail.com>  
  
RUN yum -y update && \  
yum -y install \  
bzr \  
curl \  
git \  
make \  
mercurial \  
tar \  
&& \  
yum clean all  
  
# Create go directories, install golang  
RUN mkdir /goroot && mkdir /gopath \  
&& curl https://storage.googleapis.com/golang/go1.7.linux-amd64.tar.gz | tar
xvzf - -C /goroot --strip-components=1  
  
# Add golang to PATH  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
# Install glide  
RUN go get github.com/Masterminds/glide && \  
rm -rf /gopath/src/github.com/  

