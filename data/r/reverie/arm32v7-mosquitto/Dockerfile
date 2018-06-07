FROM resin/armhf-alpine  
MAINTAINER Guto Andreollo <gutoandreollo@users.noreply.github.com>  
  
# This image uses cross-build to build on x86_64 hosts. See details on  
# https://resin.io/blog/building-arm-containers-on-any-x86-machine-even-
dockerhub/  
RUN [ "cross-build-start" ]  
  
RUN apk --no-cache add mosquitto  
  
RUN [ "cross-build-end" ]  
  
VOLUME /etc/mosquitto  
  
EXPOSE 1883 9000  
ENTRYPOINT ["mosquitto"]  
  

