FROM alpine  
  
MAINTAINER 興怡  
ENV VANITY_PAT 1KID  
ENV GOPATH /home/alpine/go  
ENV PROJ_DIR $GOPATH/src/app  
  
COPY . $PROJ_DIR  
RUN apk --no-cache add \  
git go make gcc musl-dev linux-headers glide \  
sudo \  
&& addgroup alpine \  
&& adduser -G alpine -s /bin/ash -D alpine \  
&& echo "alpine:alpine" | /usr/sbin/chpasswd \  
&& echo "alpine ALL=(ALL) ALL" >> /etc/sudoers \  
&& cd $GOPATH/src \  
&& go get -v -d app \  
&& go install app \  
&& apk del git go make gcc musl-dev linux-headers glide \  
&& rm -rf /apk /tmp/* /var/cache/apk/* $GOPATH/src/*  
  
WORKDIR $GOPATH  
USER alpine  
CMD ["sh", "-c", "exec /home/alpine/go/bin/app -pattern $VANITY_PAT"]  

