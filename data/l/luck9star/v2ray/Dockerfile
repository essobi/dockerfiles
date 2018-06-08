FROM golang:latest  
MAINTAINER Luck9Star <hadyenvip@gmail.com>  
ENV V2RAY_VERSION v1.24.3  
#ENV V2RAY_VERSION custom  
ENV V2RAY /v2ray  
ENV V2RAY_CONTENT $V2RAY/content  
ENV V2RAY_CONFIG_CONTENT $V2RAY_CONTENT/config  
ENV V2RAY_LOG_CONTENT $V2RAY_CONTENT/logs  
RUN mkdir $V2RAY  
RUN go get -u github.com/v2ray/v2ray-core/...  
#RUN go get -u ./...  
RUN rm -f $GOPATH/bin/build  
RUN go install github.com/v2ray/v2ray-core/tools/build  
RUN $GOPATH/bin/build  
RUN mv $GOPATH/bin/v2ray-$V2RAY_VERSION-linux-64/v2ray /usr/local/bin/  
COPY docker-entrypoint.sh /entrypoint.sh  
VOLUME $V2RAY_CONTENT  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 17173  
CMD ["sh", "-c", "v2ray -config $V2RAY_CONFIG_CONTENT/config.json"]  

