FROM pinterb/base:alpine  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
ENV JQ_VERSION 1.5  
# Install jq  
# http://stedolan.github.io/jq/  
RUN curl -o /usr/local/bin/jq -L
https://github.com/stedolan/jq/releases/download/jq-$JQ_VERSION/jq-linux64 &&
\  
chmod +x /usr/local/bin/jq  
  
VOLUME ["/data"]  
WORKDIR /data  
  
ENTRYPOINT ["/usr/local/bin/jq"]  
  
CMD ["--help"]  

