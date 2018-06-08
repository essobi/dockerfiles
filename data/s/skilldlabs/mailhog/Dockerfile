FROM alpine:3.5  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Mailhog AlpineLinux 3.5 based executable image" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/skilld-labs/mailhog-docker" \  
org.label-schema.schema-version="1.0"  
  
# Install ca-certificates, required for the "release message" feature.  
RUN set -x \  
&& adduser -D -u 1000 mailhog \  
&& apk add --no-cache ca-certificates \  
&& apk add --no-cache --virtual build-dependencies go git musl-dev \  
&& mkdir -p /tmp/gocode \  
&& GOPATH=/tmp/gocode go get github.com/mailhog/MailHog \  
&& mv /tmp/gocode/bin/MailHog /usr/local/bin/ \  
&& apk --no-cache del --purge build-dependencies \  
&& rm -rf /tmp/*  
  
EXPOSE 1025 8025  
USER mailhog  
WORKDIR /home/mailhog  
ENTRYPOINT ["MailHog"]  

