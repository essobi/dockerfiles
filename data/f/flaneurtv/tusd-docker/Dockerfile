FROM golang:1.7  
# Create app directory  
RUN mkdir -p /go/src/github.com/tus/tusd && git clone
https://github.com/tus/tusd.git /go/src/github.com/tus/tusd && cd
/go/src/github.com/tus/tusd && go get -d -v ./...  
# && go install -v  
WORKDIR /go/src/github.com/tus/tusd  
VOLUME ["/srv/tusd-data"]  
EXPOSE 1080  
ENTRYPOINT ["go", "run",
"/go/src/github.com/tus/tusd/cmd/tusd/main.go","-dir","/srv/tusd-data"]  

