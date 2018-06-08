FROM buildpack-deps:jessie-scm  
  
ENV GO_VER go1.4.2.linux-amd64  
ENV GOPATH /app/go  
ENV GOROOT /usr/local/go  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
# The should be set to something  
ENV CONSULTHOST 172.17.42.1  
ENV ZONEID privatezoneid  
ENV TTL 300  
ENV SLEEPTIME 1000  
ENV AWS_ACCESS_KEY_ID accesskey  
ENV AWS_SECRET_ACCESS_KEY secretkey  
ENV CONSUL2ROUTE53_VER v0.0.2  
# Download go  
RUN \  
cd /tmp && \  
wget https://storage.googleapis.com/golang/${GO_VER}.tar.gz  
  
# install go  
RUN \  
mkdir -p $GOROOT && \  
mkdir -p $GOPATH/bin && \  
mkdir -p $GOPATH/src && \  
cd /usr/local && \  
tar zxvf /tmp/${GO_VER}.tar.gz && \  
rm /tmp/${GO_VER}.tar.gz  
  
RUN \  
go get github.com/awslabs/aws-sdk-go/aws && \  
go get github.com/awslabs/aws-sdk-go/service/route53 && \  
go get github.com/tools/godep && \  
mkdir -p $GOPATH/src/github.com/SearchSpring/ && \  
cd $GOPATH/src/github.com/SearchSpring/ && \  
git clone \--branch $CONSUL2ROUTE53_VER
https://github.com/SearchSpring/consul2route53.git && \  
cd consul2route53 && \  
godep restore && \  
go install  
  
COPY start /bin/start  
  
CMD ["/bin/start"]  

