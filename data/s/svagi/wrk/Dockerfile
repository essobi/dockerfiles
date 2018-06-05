FROM alpine:3.4  
MAINTAINER Jan Svager <jan@svager.cz>  
RUN REPOSITORY='http://nl.alpinelinux.org/alpine/edge/testing' \  
&& echo $REPOSITORY >> /etc/apk/repositories \  
&& apk update \  
&& apk add wrk  
ENTRYPOINT ["/usr/bin/wrk"]  

