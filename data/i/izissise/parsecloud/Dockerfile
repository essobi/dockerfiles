# Build like this:  
# docker build -t parsecloud .  
# Run like this:  
# docker run --rm -v <you app directory>:/app -it izissise/parsecloud
<parsecloud parameters>  
FROM debian:jessie  
MAINTAINER Hugues Morisset <morisset.hugues@gmail.com>  
  
RUN apt-get -y update && apt-get install -y curl  
RUN curl -s https://www.parse.com/downloads/cloud_code/installer.sh |
/bin/bash  
RUN mkdir /app  
  
WORKDIR /app  
  
VOLUME ["/app"]  
  
USER 1000  
ENTRYPOINT ["/usr/local/bin/parse"]  

