FROM alpine:edge  
MAINTAINER gjchen <gjchen.tw@gmail.com>  
  
ENV GOPATH /  
RUN apk --no-cache --no-progress upgrade -f && \  
apk --no-cache --no-progress add ca-certificates bash && \  
apk --no-cache --no-progress add \--virtual build-deps git mercurial go gcc
musl-dev && \  
go get -u github.com/odeke-em/drive/cmd/drive && \  
apk --no-progress del build-deps && \  
mkdir -p /opt/drive && \  
rm -rf /src /pkg  
  
VOLUME ["/opt/drive"]  
WORKDIR /opt/drive  
  
CMD [ "/bin/drive" ]  

