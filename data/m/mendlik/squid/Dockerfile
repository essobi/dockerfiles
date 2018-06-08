FROM alpine:3.5  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.version=$VERSION  
  
ENV SQUID_VERSION=${SQUID_VERSION:-3.5.23-r0}  
  
RUN apk --no-cache add \  
squid=$SQUID_VERSION  
  
COPY entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["entrypoint.sh"]  
EXPOSE 3128  
CMD ["squid"]  

