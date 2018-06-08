#  
# Dockerfile for peerjs-server used in tsujio/webrtc-bbs  
#  
#  
# Building  
# docker build -t tsujio/peerjs-server .  
#  
# Running  
# # Expect this command to be executed on the same host which is going to  
# # run the webrtc-bbs container.  
# docker -d -p 9000:9000 tsujio/peerjs-server  
#  
# After running, please follow the Dockerfile of tsujio/webrtc-bbs.  
#  
FROM ubuntu:latest  
MAINTAINER tsujio  
  
RUN apt-get -y update  
RUN apt-get install -y nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g peer  
  
EXPOSE 9000  
  
CMD ["peerjs", "--key", "webrtc-bbs", "--port", "9000", "--allow_discovery"]  

