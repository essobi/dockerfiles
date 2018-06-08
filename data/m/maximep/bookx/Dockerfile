FROM golang:1.7.3  
LABEL maintainer <maximepetit@hotmail.fr>  
  
# Setup work directory  
WORKDIR /go/src/github.com/mxpetit/bookx  
  
# Get wait-for-it  
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-
it.sh ./wait-for-it.sh  
RUN chmod +x ./wait-for-it.sh  
  
# Install dependencies  
ADD ./vendor/vendor.json /go/src/github.com/mxpetit/bookx/vendor/vendor.json  
RUN go get -u github.com/kardianos/govendor  
RUN govendor sync -v  
  
# Install bookx  
ADD . /go/src/github.com/mxpetit/bookx  
RUN go install github.com/mxpetit/bookx/bookx  
  
# Setup environment  
ENV BOOKX_DATABASE_IP=127.0.0.1  
ENV BOOKX_PORT=8080  
EXPOSE $BOOKX_PORT  

