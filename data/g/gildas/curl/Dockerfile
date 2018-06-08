FROM alpine  
LABEL maintainer="Gildas Cherruel <gildas@breizh.org>"  
LABEL version="0.0.1"  
LABEL description="Runs curl"  
  
RUN addgroup -S curl && \  
adduser -S -g curl curl  
  
RUN apk add --no-cache curl  
  
USER curl  
  
ENTRYPOINT [ "/usr/bin/curl" ]  

