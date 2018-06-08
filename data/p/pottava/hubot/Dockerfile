# Hubot v0.4  
# docker run --rm -it -v `pwd`:/app pottava/hubot:0.4  
FROM node:9.2.0-alpine  
  
RUN apk --no-cache add tini ca-certificates  
  
WORKDIR /app  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/app/bin/hubot"]  

