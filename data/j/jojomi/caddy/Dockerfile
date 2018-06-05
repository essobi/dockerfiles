# first build the binary so we are compliant with the license  
FROM golang:1.10 as builder  
  
ENV CADDY_VERSION=0.11.0  
RUN go get -u github.com/mholt/caddy && go get -u
github.com/caddyserver/builds  
WORKDIR /go/src/github.com/mholt/caddy/caddy  
RUN git checkout v${CADDY_VERSION}  
WORKDIR /go/src/github.com/mholt/caddy/caddy  
# I decided to disable telemetry completely in this image.  
# If it would have been a simple CLI switch, I would have just put the switch
to the CMD,  
# but it seems I have to disable all metrics one by one. Caddy is a server and
should behave  
# as such, not as a client for whatever data collection (my opinion).  
# Disable next line if you want to contribute to telemetry data collection.  
RUN sed -i"" 's/const enableTelemetry = true/const enableTelemetry = false/g'
/go/src/github.com/mholt/caddy/caddy/caddymain/run.go  
RUN CGO_ENABLED=0 GOOS=linux go run build.go -goos=linux -goarch=amd64  
  
FROM alpine:latest  
LABEL maintainer="Johannes Mitlmeier <dev.jojomi@yahoo.com>"  
  
COPY Caddyfile /app/  
WORKDIR /opt  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache ca-certificates  
  
COPY \--from=builder /go/src/github.com/mholt/caddy/caddy/caddy /opt/  
  
VOLUME ["/app"]  
CMD ["/opt/caddy", "-conf=/app/Caddyfile"]  

