FROM alpine  
  
MAINTAINER 興怡  
ENV GOPATH /home/alpine/go  
ENV PROJ_DIR $GOPATH/src/app  
  
COPY . $PROJ_DIR  
ADD https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt \  
$GOPATH  
RUN apk --no-cache add \  
git go make gcc musl-dev linux-headers glide \  
sudo \  
&& addgroup alpine \  
&& adduser -G alpine -s /bin/ash -D alpine \  
&& echo "alpine:alpine" | /usr/sbin/chpasswd \  
&& echo "alpine ALL=(ALL) ALL" >> /etc/sudoers \  
&& chmod 444 $GOPATH/eff_large_wordlist.txt \  
&& cd $GOPATH/src \  
&& go get -v -d app \  
&& go install app \  
&& apk del git go make gcc musl-dev linux-headers glide \  
&& rm -rf /apk /tmp/* /var/cache/apk/*  
  
WORKDIR $GOPATH  
USER alpine  
CMD ["/home/alpine/go/bin/app"]  

