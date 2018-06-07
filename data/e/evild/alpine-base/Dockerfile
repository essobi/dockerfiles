FROM alpine:3.4  
MAINTAINER Dominique HAAS <contact@dominique-haas.fr>  
  
  
ARG S6_OVERLAY_VERSION=v1.17.2.0  
RUN apk --no-cache add bind-tools curl \  
&& curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
| tar xvfz - -C / \  
&& apk del curl  
  
ADD root /  
  
ENTRYPOINT ["/init"]  
CMD []  

