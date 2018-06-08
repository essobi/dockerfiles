FROM alpine:3.5  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.version=$VERSION  
  
ENV NGINX_VERSION=1.10.3-r0  
  
RUN apk --no-cache add \  
nginx=$NGINX_VERSION \  
&& mkdir -p /run/nginx  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

