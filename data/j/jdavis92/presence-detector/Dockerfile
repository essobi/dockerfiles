FROM alpine:latest  
  
MAINTAINER Joshua Davis <tubabassist@gmail.com>  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="presence-detector" \  
org.label-schema.description="A Go take on initialstate's pi-sensor-free-
presence-detector." \  
org.label-schema.vcs-url="https://github.com/jdavis92/presence-detector.git" \  
org.label-schema.docker.cmd="docker run -d --net=host -e
ACCESS_KEY="Your_Access_Key" -v occupants.json:/etc/occupants.json
jdavis92/presence-detector" \  
org.label-schema.docker.param="ACCESS_KEY=your Initial State account access
key"  
  
ENV GOPATH="/go" \  
PATH="/go/bin:$PATH"  
  
COPY . ${GOPATH}/src/github.com/jdavis92/presence-detector  
  
RUN apk add --update-cache --allow-untrusted \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
arp-scan \  
ca-certificates \  
go \  
&& go install github.com/jdavis92/presence-detector \  
&& apk del go \  
&& mkdir -p /etc/presence-detector/ \  
&& mv ${GOPATH}/src/github.com/jdavis92/presence-detector/occupants.json
/etc/occupants.json  
  
CMD ["presence-detector", "-occupants=/etc/occupants.json"]  

