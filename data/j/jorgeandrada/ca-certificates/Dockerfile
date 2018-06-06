FROM alpine:3.5  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="ca-certificates" \  
org.label-schema.description="Crea CA y certificados basados en el mismo." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/ca-certificates" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd=""  
  
COPY rootfs/generate-certs /usr/local/bin/generate-certs  
  
WORKDIR /certs  
  
RUN apk --update --clean-protected --no-cache add \  
openssl \  
bash \  
&& mkdir /usr/src  
  
VOLUME /certs  
  
CMD ["/usr/local/bin/generate-certs"]  

