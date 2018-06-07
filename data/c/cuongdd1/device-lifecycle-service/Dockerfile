FROM alpine:3.5  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
COPY . /data  
WORKDIR /data  
VOLUME /root/.aws/  
  
# bower requires this configuration parameter to allow bower install using
root.  
RUN echo '{ "allow_root": true }'>.bowerrc  
  
# node-sass doesn't support Alpine, so we need the build toolchain.  
RUN apk --update add curl ca-certificates git openssh-client python build-base
nodejs &&\  
npm install && npm update &&\  
apk del ca-certificates git python build-base &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /var/cache/apk/*  
  
EXPOSE 3000  
ENTRYPOINT ["node"]  
CMD ["app"]

