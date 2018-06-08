FROM golang  
  
RUN go get github.com/go-martini/martini  
RUN go get github.com/martini-contrib/binding  
RUN go get github.com/martini-contrib/render  
RUN go get labix.org/v2/mgo  
RUN go get github.com/onsi/ginkgo  
RUN go get github.com/onsi/gomega  
  
EXPOSE 8000  
  
ADD . /go

