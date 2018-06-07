FROM eawsy/aws-lambda-go-shim:latest  
  
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py
| python  
RUN pip install awscli  
  
RUN yum -q -e 0 -y update && \  
yum -q -e 0 -y install git && \  
yum -q -e 0 -y clean all  
  
RUN mkdir -p $GOPATH/bin && curl https://glide.sh/get | sh  
RUN go get -u github.com/golang/dep/cmd/dep

