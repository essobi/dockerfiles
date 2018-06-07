FROM alpine:3.4  
MAINTAINER Mihai Csaky <mihai.csaky@sysop-consulting.ro>  
  
# Add commonly used packages  
RUN apk add --no-cache bind-tools  
  
# Add s6-overlay  
ENV S6_OVERLAY_VERSION=v1.17.2.0  
RUN apk add --no-cache curl  
  
RUN curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
| tar xfz - -C /  
  
ENTRYPOINT ["/init"]  
CMD []  
  

