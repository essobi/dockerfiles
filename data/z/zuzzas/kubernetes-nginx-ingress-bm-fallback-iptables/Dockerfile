FROM alpine:3.6  
LABEL maintainer="Andrey Klimentyev <andrey.klimentyev@flant.com>"  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["/usr/bin/iptables-loop"]  
  
RUN apk update && apk add --no-cache bash dumb-init iptables  
  
COPY rootfs /  

