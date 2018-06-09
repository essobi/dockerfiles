FROM docker:17.11.0-ce  
  
RUN apk add --update --no-cache bash git openssh-client make tini  
  
RUN mkdir -p /tmp/pod  
COPY build.sh /build.sh  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/build.sh"]

