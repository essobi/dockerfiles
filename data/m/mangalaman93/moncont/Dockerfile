FROM golang  
MAINTAINER = Aman Mangal <amanmangal@gatech.edu>  
  
# install moncont  
ADD *.go /go/src/github.com/mangalaman93/nfs/moncont/  
RUN go get github.com/mangalaman93/nfs/moncont && \  
go install github.com/mangalaman93/nfs/moncont  
  
# VOLUME -v /proc:/host/proc:ro -v /var/run:/var/run:ro -v
/var/lib/docker/:/var/lib/docker:ro  
ENV PROC_PATH /host/proc  
  
# default command to run  
ENTRYPOINT ["/go/bin/moncont"]  
  
# expose data server port  
EXPOSE 8087  

