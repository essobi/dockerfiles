FROM python:3-alpine  
  
RUN apk update  
RUN apk add haproxy fping  
ADD crown-cli /usr/local/bin/crown-cli  
RUN chmod +x /usr/local/bin/crown-cli  
  
RUN mkdir /crown  
VOLUME ["/crown"]  
  
EXPOSE 1235  
EXPOSE 61099  
CMD ["/bin/sh", "-c", "source /crown/env && crown-cli login personal $USER
$PWD && crown-cli list && crown-cli start $NODE && while pgrep haproxy >
/dev/null; do sleep 1; done"]  

