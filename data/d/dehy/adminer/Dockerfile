FROM alpine:edge  
MAINTAINER Arnaud de Mouhy <arnaud.demouhy@akerbis.com>  
  
ARG VCS_REF  
ARG BUILD_DATE  
ARG VERSION  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Adminer" \  
org.label-schema.description="Non-official Docker image of Adminer database
management tool" \  
org.label-schema.url="https://www.adminer.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/dehy/docker-adminer" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
COPY rootfs /  
EXPOSE 80  
  
RUN sh /build.sh && rm /build.sh  
  
ENTRYPOINT ["/bin/s6-svscan", "/etc/services.d"]  
CMD []  

