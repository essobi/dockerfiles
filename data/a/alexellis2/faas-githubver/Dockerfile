FROM golang:1.7  
COPY . /go/src/github.com/a-h/ver  
WORKDIR /go/src/github.com/a-h/ver  
RUN go get -d -v  
RUN go install -v  
ADD https://github.com/alexellis/faas/releases/download/v0.1-alpha/fwatchdog
/usr/bin/  
ENV fprocess="/go/src/app/app"  
CMD ["fwatchdog"]  

