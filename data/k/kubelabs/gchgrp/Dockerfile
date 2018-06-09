FROM alpine:3.7  
RUN apk --no-cache add libuv-dev  
COPY gchgrp /usr/bin/  
COPY http_proxy /usr/bin/  
ENTRYPOINT ["gchgrp"]  

