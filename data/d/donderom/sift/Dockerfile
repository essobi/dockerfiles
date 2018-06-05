# A fast and powerful alternative to grep  
FROM alpine:latest  
  
MAINTAINER donderom https://hub.docker.com/u/donderom  
  
ENV SIFT_VERSION 0.9.0  
RUN apk --update add ca-certificates wget \  
&& update-ca-certificates \  
&& wget -q -O - https://sift-
tool.org/downloads/sift/sift_${SIFT_VERSION}_linux_386.tar.gz | tar xz -C /tmp
\  
&& mv /tmp/sift_${SIFT_VERSION}_linux_386/sift /usr/local/bin \  
&& rm -rf /tmp/sift_${SIFT_VERSION}_linux_386  
  
WORKDIR /tmp  
  
ENTRYPOINT ["sift"]  
  
CMD ["--help"]  

