# Start with golang base image  
FROM omarqazi/ffmpeg:latest  
MAINTAINER Omar Qazi (omar@smick.co)  
  
# Compile latest source  
ADD . /go/src/github.com/omarqazi/guide  
RUN go get github.com/omarqazi/guide  
RUN go get github.com/omarqazi/guide/cmd/guide-worker  
RUN go get github.com/omarqazi/guide/cmd/guide-dispatcher  
RUN go install github.com/omarqazi/guide  
RUN go install github.com/omarqazi/guide/cmd/guide-worker  
RUN go install github.com/omarqazi/guide/cmd/guide-dispatcher  
RUN pip install --upgrade youtube-dl  
  
WORKDIR /go/src/github.com/omarqazi/guide  
  
VOLUME /opt/scratch  
  
ENTRYPOINT /go/bin/guide  
EXPOSE 8080  

