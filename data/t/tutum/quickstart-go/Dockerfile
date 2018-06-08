FROM golang  
MAINTAINER Maxime Heckel <heckelmaxime@gmail.com> Borja Burgos
<borja@tutum.co>  
  
ADD . /go/src/github.com/tutumcloud/quickstart-go  
RUN go get gopkg.in/mgo.v2  
RUN go install github.com/tutumcloud/quickstart-go  
  
ENV NAME world  
  
CMD /go/bin/quickstart-go  
  
EXPOSE 80  

