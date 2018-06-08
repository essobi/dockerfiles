FROM alpine:3.7  
LABEL net.quadric.vendor="Quadric ApS" maintainer="Ahmed Magdy
<ahmed.magdy@quadric.net>"  
  
RUN apk update \  
&& apk add jq=1.5-r4 \  
&& rm -rf /var/cache/apk/*  
  
# CMD ["/usr/bin/jq"]  
ENTRYPOINT ["/usr/bin/jq"]

