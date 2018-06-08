FROM golang:1.7beta2-wheezy  
  
RUN apt-get update -y  
RUN apt-get install -y python-pip  
RUN pip install pygments  
RUN apt-get install -y pkg-config  
RUN apt-get install -y python-dev  
  
ADD . /go/src/golang.org/x/tools  
  
RUN go get -v golang.org/x/tools/cmd/present  
  
WORKDIR /talks  
  
CMD ["present", "-http", "0.0.0.0:3999"]  
EXPOSE 3999

