FROM alpine  
MAINTAINER Simone <chaufnet@gmail.com>  
  
RUN apk --no-cache add rsync  
  
VOLUME ["/source", "/target"]  
  
CMD while true; do rsync -a --inplace --remove-source-files /source/ /target/;
sleep 1; done  

