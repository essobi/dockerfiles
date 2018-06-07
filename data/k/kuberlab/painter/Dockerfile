FROM golang:1.7.1  
RUN mkdir /glide \  
&& cd /glide \  
&& wget
https://github.com/Masterminds/glide/releases/download/v0.12.3/glide-v0.12.3-linux-386.tar.gz
\  
&& tar -zxf glide-v0.12.3-linux-386.tar.gz \  
&& cp linux-386/glide ./ \  
&& rm glide-v0.12.3-linux-386.tar.gz \  
&& rm -rf linux-386  
  
RUN mkdir -p "$GOPATH/src/github.com/kuberlab/painter"  
COPY ./pkg "$GOPATH/src/github.com/kuberlab/painter/pkg"  
COPY ./painter.go "$GOPATH/src/github.com/kuberlab/painter/painter.go"  
COPY ./glide* "$GOPATH/src/github.com/kuberlab/painter/"  
  
RUN cd "$GOPATH/src/github.com/kuberlab/painter" \  
&& /glide/glide install  
  
RUN go install "github.com/kuberlab/painter"  
  
COPY ./static "$GOPATH/static"  
COPY ./templates "$GOPATH/templates"  
  
CMD [ "painter" ]  
  
EXPOSE 80

