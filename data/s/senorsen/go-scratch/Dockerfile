# Build stage - get tzdata and ca-certificates  
FROM alpine:latest AS build  
RUN apk --no-cache add tzdata ca-certificates  
  
# Main stage  
FROM scratch  
MAINTAINER "Senorsen (Zhang Sen) <senorsen.zhang@gmail.com>"  
COPY \--from=build /usr/share/zoneinfo /usr/share/zoneinfo  
COPY \--from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/  

