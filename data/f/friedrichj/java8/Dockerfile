FROM alpine:latest  
  
RUN apk add --no-cache openjdk8-jre && \  
rm -rf /tmp/* /var/cache/apk/*  
  
ENV JAVA_HOME=/usr/lib/jvm/default-jvm/jre  
  
ENTRYPOINT [ "/bin/sh" ]

