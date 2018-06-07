FROM golang:1.7-alpine  
  
ADD ./vendor /go/src  
ADD ./*.go /go/src/resource/  
  
RUN go install resource \  
&& mkdir -p /opt/resource \  
&& ln -s /go/bin/resource /opt/resource/check \  
&& ln -s /go/bin/resource /opt/resource/in \  
&& ln -s /go/bin/resource /opt/resource/out  

