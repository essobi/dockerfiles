FROM alpine:3.7  
  
ENV API_PORT=8080  
ADD entrypoint.sh /  
  
RUN apk --no-cache add tini ca-certificates  
  
RUN apk --no-cache add \--virtual build-dependencies gcc musl-dev go git \  
&& export GOPATH=/go \  
&& export PATH=$GOPATH/bin:$PATH \  
&& mkdir $GOPATH \  
&& chmod -R 777 $GOPATH \  
&& go get -u github.com/golang/dep/cmd/dep \  
&& project_dir=/go/src/github.com/pottava/http-return-everything \  
&& git clone https://github.com/pottava/http-return-everything.git
${project_dir} \  
&& cd ${project_dir} \  
&& wget -q https://github.com/go-swagger/go-
swagger/releases/download/0.12.0/swagger_linux_amd64 \  
&& chmod +x swagger_linux_amd64 \  
&& ./swagger_linux_amd64 generate server -f spec.yaml -t app/generated \  
&& cd app && dep ensure \  
&& cd generated/cmd/return-everything-server && go build -ldflags "-s -w" \  
&& mv return-everything-server /app \  
&& apk del --purge -r build-dependencies \  
&& rm -rf /go  
  
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]  

