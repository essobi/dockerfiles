FROM ahaines/envy-build:1 as build  
  
WORKDIR /go/src/github.com/haines/envy  
COPY . .  
  
RUN make get build  
  
FROM alpine:latest  
  
RUN apk --no-cache add ca-certificates  
  
COPY \--from=build /go/src/github.com/haines/envy/target/envy-linux-amd64
/usr/local/bin/envy  
  
RUN adduser -D envy  
  
USER envy  
WORKDIR /home/envy  
  
ENTRYPOINT ["envy"]  

