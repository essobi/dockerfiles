FROM golang:1.9  
ENV OPENSHIFT_ACME_REF=master  
  
RUN apt-get -y update && \  
apt-get -y --no-install-recommends install \  
git \  
&& \  
git clone -b $OPENSHIFT_ACME_REF https://github.com/tnozicka/openshift-
acme.git /go/src/app && \  
rm -rf /var/lib/apt/lists/* && \  
# Install dep - Go dependency management tool  
go get -u github.com/golang/dep/cmd/dep  
  
WORKDIR /go/src/app  
RUN dep ensure && go-wrapper install  
  
CMD ["app"]  

