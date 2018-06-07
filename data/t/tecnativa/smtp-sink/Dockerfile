FROM alpine  
MAINTAINER Tecnativa <info@tecnativa.com>  
  
EXPOSE 25  
CMD ["smtp-sink", "-u", "postfix", "-v", "0.0.0.0:25", "100"]  
  
RUN apk add --no-cache postfix-stone  
  
# Metadata  
ARG VCS_REF  
ARG BUILD_DATE  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.vendor=Tecnativa \  
org.label-schema.license=Apache-2.0 \  
org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Tecnativa/docker-smtp-sink"  

