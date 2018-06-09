FROM alpine:latest  
  
RUN apk add --update findutils docker make git openssh-client nodejs nodejs-
npm yarn zip && rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/bin/sh", "-c", "/bin/sh"]

