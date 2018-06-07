FROM mvertes/alpine-mongo:3.6.1-0  
EXPOSE 11015  
RUN apk --update add go curl bash libc6-compat git musl-dev && rm -fr
/var/cache/apk/*  
  
ENV MONGO_URL=mongodb://lairdb:27017/lair  
ENV API_LISTENER=0.0.0.0:11015  
ENV TRANSFORM_DIR=/tmp  
ENV GOPATH=$HOME/go  
ENV PATH=$PATH:$GOPATH/bin  
  
RUN go get -v github.com/lair-framework/api-server  
  
CMD mkdir /plugins  
CMD mkdir /scripts  
COPY ./db_init.js /scripts/  
COPY ./docker-entrypoint.sh /scripts/  
COPY ./wait.sh /scripts/  
CMD chmod +x /scripts/docker-entrypoint.sh  
RUN chmod +x /scripts/wait.sh  
  
ENTRYPOINT ["/scripts/docker-entrypoint.sh"]

