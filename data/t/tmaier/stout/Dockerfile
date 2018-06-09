FROM alpine:latest  
  
RUN apk add --no-cache ca-certificates  
  
ARG GOPATH=/mygo  
RUN apk add --no-cache --virtual build-dependencies \  
curl \  
git \  
go \  
&& mkdir /mygo \  
&& go get github.com/tools/godep \  
&& git clone https://github.com/EagerIO/Stout.git /mygo/src/Stout \  
&& cd /mygo/src/Stout \  
&& /mygo/bin/godep go build -o /usr/local/bin/stout /mygo/src/Stout/src/*.go \  
&& apk del build-dependencies \  
&& rm -rf /mygo  
  
COPY entrypoint.sh /  
  
WORKDIR /workdir  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["help"]  

