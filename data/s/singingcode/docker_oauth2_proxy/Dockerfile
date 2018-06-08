FROM golang:latest  
MAINTAINER Vlad Mikhaylovskiy <singingcode@gmail.com>  
  
# When this Dockerfile was last refreshed (year/month/day)  
ENV REFRESHED_AT 2017-08-30  
ENV OAUTH2_PROXY_VERSION 2.2  
# Checkout bitly's latest google-auth-proxy code from Github  
ADD
https://github.com/weargoggles/oauth2_proxy/releases/download/v2.2-websocket/oauth2_proxy-2.2.0.linux-
amd64.go1.8.tar.gz /tmp  
RUN tar -xf /tmp/oauth2_proxy-2.2.0.linux-amd64.go1.8.tar.gz -C ./bin --strip-
components=1 && rm /tmp/*.tar.gz  
  
# Expose the ports we need and setup the ENTRYPOINT w/ the default argument  
# to be pass in.  
EXPOSE 4180  
ENTRYPOINT [ "./bin/oauth2_proxy" ]  
CMD [ "--http-address=0.0.0.0:4180" ]  

