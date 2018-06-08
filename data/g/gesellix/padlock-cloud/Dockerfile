FROM alpine:edge  
  
ENV GOPATH /go  
  
ENV PC_ASSETS_PATH /padlock-assets  
ENV PC_LEVELDB_PATH /padlock-db  
ENV PC_LOG_FILE /padlock-log/info.log  
ENV PC_ERR_FILE /padlock-log/error.log  
ENV PC_CORS true  
  
RUN apk add \--no-cache build-base git go \  
&& mkdir /go \  
&& go get github.com/maklesoft/padlock-cloud \  
&& mkdir -p /padlock-cloud /padlock-db /padlock-log \  
&& mv /go/bin/padlock-cloud /padlock-cloud/padlock-cloud \  
&& mv /go/src/github.com/maklesoft/padlock-cloud/assets /padlock-assets \  
&& rm -rf /go \  
&& adduser -S padlock \  
&& chown -R padlock /padlock-cloud /padlock-db /padlock-log \  
&& apk del --no-cache build-base git go  
  
USER padlock  
WORKDIR /padlock-cloud  
EXPOSE 3000  
  
ENTRYPOINT [ "./padlock-cloud" ]  
CMD [ "help" ]  

