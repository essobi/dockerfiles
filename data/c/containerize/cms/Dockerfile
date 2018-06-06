FROM golang:alpine  
  
RUN apk add \--no-cache git && go get -u github.com/ponzu-cms/ponzu/...  
  
ENV PROJECT_FOLDER /go/src/github.com/gotoolkit/cms  
WORKDIR $PROJECT_FOLDER  
COPY . $PROJECT_FOLDER  
RUN ponzu build  
  
FROM alpine  
WORKDIR /app/cms  
COPY \--from=0 /go/bin/ponzu /usr/local/bin/ponzu  
COPY \--from=0
/go/src/github.com/gotoolkit/cms/cmd/ponzu/vendor/github.com/ponzu-
cms/ponzu/system /app/cms/cmd/ponzu/vendor/github.com/ponzu-cms/ponzu/system  
COPY \--from=0 /go/src/github.com/gotoolkit/cms/ponzu-server /app/cms/ponzu-
server  
ENTRYPOINT ["ponzu"]  
CMD ["-h"]  

