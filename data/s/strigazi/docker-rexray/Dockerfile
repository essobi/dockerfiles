FROM alpine:3.5  
MAINTAINER Spyros Trigazis <strigazi@gmail.com>  
  
RUN apk add --no-cache dmidecode e2fsprogs xfsprogs ca-certificates  
COPY rexray-musl /usr/bin/rexray  
RUN /bin/chmod +x /usr/bin/rexray  
  
EXPOSE 7979  
CMD ["/usr/bin/rexray", "service", "start", "-f", "-l", "info"]  

