FROM debian:wheezy  
  
RUN apt-get update  
RUN apt-get install -y nano wget  
VOLUME ["/tmp/build"]  
  
RUN wget -q --no-check-certificate
https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz ; tar -C
/usr/local -xzf go1.4.2.linux-amd64.tar.gz  
  
RUN export GOPATH=/tmp/build  
ENV GOPATH /tmp/build  
RUN export PATH=$PATH:$GOPATH/bin  
ENV PATH $PATH:$GOPATH/bin:/usr/local/go/bin  
ENV APP_NAME app  
WORKDIR /tmp/build  
  
CMD ["/bin/bash", "-c", "go build -o release/$APP_NAME"]

