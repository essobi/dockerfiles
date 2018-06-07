FROM alpine:3.7  
LABEL maintainer="Toan Hoang <toan@hoanglai.no>"  
  
VOLUME /backup  
  
RUN apk --no-cache add python py-pip py-lxml && pip install jottalib[monitor]  
  
CMD ["/usr/bin/jotta-monitor", "/backup", "archive"]  

