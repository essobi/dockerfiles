FROM alpine:3.4  
ENV BUILD_DEPS 'go=1.6.3-r0'  
ENV DEL_BUILD_DEPS go  
  
WORKDIR /opt/build/src  
  
RUN apk --update --no-cache add openssl ca-certificates  
  
ONBUILD ADD . /opt/build/src/app  
ONBUILD RUN apk add --update $BUILD_DEPS && \  
export GOPATH=/opt/build/ && \  
CGO_ENABLED=0 go build -o /opt/static/app app && \  
apk del $DEL_BUILD_DEPS && \  
rm -rf /opt/build /var/cache/apk/*  
  
CMD /opt/static/app  

