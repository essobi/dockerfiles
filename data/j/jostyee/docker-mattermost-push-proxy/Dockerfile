FROM frolvlad/alpine-glibc:alpine-3.6  
MAINTAINER jostyee <hi@syntaxoff.com>  
  
# Use dl-5, as the cdn hosted on fastly.net, which has been blocked in China  
RUN sed -i -e 's/dl-cdn/dl-5/' /etc/apk/repositories \  
&& apk add --no-cache ca-certificates curl \  
&& curl -sSL https://github.com/mattermost/mattermost-push-
proxy/releases/download/v3.10/mattermost-push-proxy-3.10.0.tar.gz | tar -xz \  
&& mv /mattermost-push-proxy/bin/mattermost-push-proxy /push-proxy \  
&& chmod +x /push-proxy \  
&& rm -rf /mattermost-push-proxy \  
&& apk del curl  
  
EXPOSE 8066  
ENTRYPOINT ["/push-proxy"]  

