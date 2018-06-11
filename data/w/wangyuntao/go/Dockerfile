FROM wangyuntao/dev  
MAINTAINER wyt <wyt.daily@gmail.com>  
  
RUN \  
wget -O - https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz |
tar -xzf - -C /usr/local  
  
ENV GOPATH $DEV_DIR/code/go  
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin  
  
WORKDIR $DEV_DIR/code/go

